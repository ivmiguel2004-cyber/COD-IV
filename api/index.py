"""
COD-IV — API principal (FastAPI).

Rotas:
  POST /api/cadastro          -> cria utilizador
  POST /api/login             -> autentica, devolve token
  POST /api/quiz/iniciar      -> cria sessão de quiz + devolve perguntas
  POST /api/quiz/responder    -> guarda resposta a uma pergunta (ou skip)
  POST /api/quiz/finalizar    -> fecha sessão, calcula perguntas saltadas como erradas
  GET  /api/quiz/{id}/resultados -> devolve resultado detalhado da sessão
"""
import os
from datetime import datetime, timezone
from typing import List

import jwt
from fastapi import FastAPI, Depends, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session, joinedload

import models
import schemas
import auth
import quiz_logic
from database import Base, engine, get_db

# Cria as tabelas se ainda não existirem (idempotente)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="COD-IV API")

# CORREÇÃO: CORS agora lê o(s) domínio(s) permitido(s) da env var
# COD_IV_ALLOWED_ORIGINS (separados por vírgula), ex:
#   COD_IV_ALLOWED_ORIGINS=https://cod-iv.vercel.app,https://cod-iv-tuo.dominio.co.ao
# Sem essa variável definida, mantém "*" (só serve para desenvolvimento/demo).
_origins_env = os.environ.get("COD_IV_ALLOWED_ORIGINS")
_allowed_origins = [o.strip() for o in _origins_env.split(",")] if _origins_env else ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=_allowed_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------- Dependência: utilizador autenticado ----------
def utilizador_atual(
    authorization: str = Header(default=None),
    db: Session = Depends(get_db),
) -> models.Utilizador:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token em falta.")
    token = authorization.removeprefix("Bearer ").strip()
    try:
        utilizador_id = auth.validar_token(token)
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Sessão expirada. Faz login novamente.")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido.")

    utilizador = db.get(models.Utilizador, utilizador_id)
    if not utilizador:
        raise HTTPException(status_code=401, detail="Utilizador não encontrado.")
    return utilizador


# ---------- Cadastro / Login ----------
@app.post("/api/cadastro", response_model=schemas.AuthResponse)
def cadastro(payload: schemas.CadastroRequest, db: Session = Depends(get_db)):
    username = auth.gerar_username_unico(db, payload.primeiro_nome, payload.ultimo_nome)
    novo = models.Utilizador(
        primeiro_nome=payload.primeiro_nome.strip(),
        ultimo_nome=payload.ultimo_nome.strip(),
        username=username,
        password_hash=auth.hash_password(payload.password),
    )
    db.add(novo)
    db.commit()
    db.refresh(novo)

    token = auth.criar_token(novo.id)
    return schemas.AuthResponse(token=token, utilizador=novo)


@app.post("/api/login", response_model=schemas.AuthResponse)
def login(payload: schemas.LoginRequest, db: Session = Depends(get_db)):
    candidatos = (
        db.query(models.Utilizador)
        .filter(
            models.Utilizador.primeiro_nome == payload.primeiro_nome.strip(),
            models.Utilizador.ultimo_nome == payload.ultimo_nome.strip(),
        )
        .all()
    )
    # Nomes podem repetir-se: testa a password contra todos os candidatos
    utilizador_valido = None
    for candidato in candidatos:
        if auth.verify_password(payload.password, candidato.password_hash):
            utilizador_valido = candidato
            break

    if not utilizador_valido:
        raise HTTPException(status_code=401, detail="Nome ou password incorretos.")

    token = auth.criar_token(utilizador_valido.id)
    return schemas.AuthResponse(token=token, utilizador=utilizador_valido)


# ---------- Quiz ----------
@app.post("/api/quiz/iniciar", response_model=schemas.QuizSessionOut)
def iniciar_quiz(
    payload: schemas.IniciarQuizRequest,
    db: Session = Depends(get_db),
    utilizador: models.Utilizador = Depends(utilizador_atual),
):
    try:
        num_perguntas = quiz_logic.validar_num_perguntas(payload.num_perguntas)
        perguntas = quiz_logic.selecionar_perguntas(db, payload.materia, num_perguntas)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    tempo_total = quiz_logic.calcular_tempo_total(num_perguntas)

    session = models.QuizSession(
        utilizador_id=utilizador.id,
        materia=payload.materia,
        num_perguntas=num_perguntas,
        tempo_total_segundos=tempo_total,
        status="em_progresso",
    )
    db.add(session)
    db.flush()

    # Cria já as linhas de resposta (vazias) para cada pergunta, na ordem sorteada
    for ordem, pergunta in enumerate(perguntas):
        db.add(models.QuizResposta(
            quiz_session_id=session.id,
            pergunta_id=pergunta.id,
            ordem=ordem,
            opcoes_escolhidas=[],
            correta=None,
            saltada=False,
        ))
    db.commit()
    db.refresh(session)

    session.perguntas = perguntas  # anexa para a resposta (não persistido, só serialização)
    return session


@app.post("/api/quiz/responder")
def responder_pergunta(
    quiz_session_id: int,
    payload: schemas.ResponderPerguntaRequest,
    db: Session = Depends(get_db),
    utilizador: models.Utilizador = Depends(utilizador_atual),
):
    session = _obter_sessao_do_utilizador(db, quiz_session_id, utilizador)
    if session.status != "em_progresso":
        raise HTTPException(status_code=400, detail="Esta sessão já foi finalizada.")

    resposta = (
        db.query(models.QuizResposta)
        .filter_by(quiz_session_id=session.id, pergunta_id=payload.pergunta_id)
        .first()
    )
    if not resposta:
        raise HTTPException(status_code=404, detail="Pergunta não pertence a esta sessão.")

    pergunta = db.get(
        models.QuizPergunta, payload.pergunta_id,
        options=[joinedload(models.QuizPergunta.opcoes)],
    )

    if payload.saltada:
        resposta.saltada = True
        resposta.opcoes_escolhidas = []
        resposta.correta = None
    else:
        resposta.saltada = False
        resposta.opcoes_escolhidas = payload.opcoes_escolhidas
        resposta.correta = quiz_logic.avaliar_resposta(pergunta, payload.opcoes_escolhidas)
        resposta.respondida_em = datetime.now(timezone.utc)

    db.commit()
    return {"ok": True}


@app.post("/api/quiz/{quiz_session_id}/finalizar", response_model=schemas.ResultadoQuizOut)
def finalizar_quiz(
    quiz_session_id: int,
    db: Session = Depends(get_db),
    utilizador: models.Utilizador = Depends(utilizador_atual),
):
    session = _obter_sessao_do_utilizador(db, quiz_session_id, utilizador)
    if session.status == "finalizado":
        return _montar_resultado(db, session)

    # Qualquer pergunta saltada e nunca respondida até agora conta como errada
    respostas = db.query(models.QuizResposta).filter_by(quiz_session_id=session.id).all()
    for r in respostas:
        if r.correta is None:
            r.correta = False
            r.saltada = True

    session.status = "finalizado"
    session.finalizado_em = datetime.now(timezone.utc)
    db.commit()

    return _montar_resultado(db, session)


@app.get("/api/quiz/{quiz_session_id}/resultados", response_model=schemas.ResultadoQuizOut)
def obter_resultados(
    quiz_session_id: int,
    db: Session = Depends(get_db),
    utilizador: models.Utilizador = Depends(utilizador_atual),
):
    session = _obter_sessao_do_utilizador(db, quiz_session_id, utilizador)
    return _montar_resultado(db, session)


# ---------- Auxiliares internos ----------
def _obter_sessao_do_utilizador(db: Session, quiz_session_id: int, utilizador: models.Utilizador) -> models.QuizSession:
    session = db.get(models.QuizSession, quiz_session_id)
    if not session or session.utilizador_id != utilizador.id:
        raise HTTPException(status_code=404, detail="Sessão de quiz não encontrada.")
    return session


def _montar_resultado(db: Session, session: models.QuizSession) -> schemas.ResultadoQuizOut:
    respostas = (
        db.query(models.QuizResposta)
        .filter_by(quiz_session_id=session.id)
        .order_by(models.QuizResposta.ordem)
        .all()
    )

    # CORREÇÃO: antes fazia 1 query (com join) por cada resposta — para um
    # quiz de 50 perguntas eram 50 queries. Agora carrega todas de uma vez.
    perguntas_por_id = {
        p.id: p
        for p in db.query(models.QuizPergunta)
        .options(joinedload(models.QuizPergunta.opcoes))
        .filter(models.QuizPergunta.id.in_([r.pergunta_id for r in respostas]))
        .all()
    }

    respostas_out: List[schemas.RespostaResultadoOut] = []
    total_certas = 0
    for r in respostas:
        pergunta = perguntas_por_id[r.pergunta_id]
        corretas_ids = [o.id for o in pergunta.opcoes if o.correta]
        if r.correta:
            total_certas += 1

        respostas_out.append(schemas.RespostaResultadoOut(
            pergunta_id=pergunta.id,
            enunciado=pergunta.enunciado,
            imagem_url=pergunta.imagem_url,
            opcoes=[schemas.OpcaoOut.model_validate(o) for o in pergunta.opcoes],
            opcoes_corretas_ids=corretas_ids,
            opcoes_escolhidas_ids=r.opcoes_escolhidas or [],
            correta=bool(r.correta),
            saltada=r.saltada,
        ))

    return schemas.ResultadoQuizOut(
        quiz_session_id=session.id,
        materia=session.materia,
        total_perguntas=len(respostas),
        total_certas=total_certas,
        total_erradas=len(respostas) - total_certas,
        respostas=respostas_out,
    )


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.post("/api/admin/seed")
def popular_base_de_dados(key: str):
    """
    Popula a base de dados de produção (sinais, mecânica, perguntas Tipo B/C)
    sem precisar de correr nada no teu computador.

    Protegido por COD_IV_ADMIN_SEED_KEY (define esta variável de ambiente no
    Vercel com uma password à tua escolha). Depois do deploy, chama-se assim
    no browser: https://o-teu-site.vercel.app/api/admin/seed?key=A_TUA_CHAVE

    É seguro chamar mais do que uma vez: cada função de seed_db.py já
    verifica se os dados existem antes de os inserir de novo.
    """
    chave_esperada = os.environ.get("COD_IV_ADMIN_SEED_KEY")
    if not chave_esperada or key != chave_esperada:
        raise HTTPException(status_code=403, detail="Chave inválida ou COD_IV_ADMIN_SEED_KEY não definida.")

    import seed_db
    seed_db.main()
    return {"status": "ok", "mensagem": "Base de dados populada (ou já estava)."}


# CORREÇÃO / CONVENIÊNCIA PARA DESENVOLVIMENTO LOCAL:
# Em produção no Vercel, o vercel.json já serve a pasta public/ diretamente
# (routes: "/(.*)" -> "public/$1"), sem passar por aqui — este mount nunca é
# usado nesse caso. Mas para testar tudo no teu computador com um único
# comando (sem instalar Node/Vercel CLI), montamos a pasta public/ aqui, para
# que "uvicorn index:app" sirva o site inteiro (HTML+CSS+JS) e a API na
# mesma origem em http://localhost:8000/. Fica DEPOIS de todas as rotas
# /api/..., por isso não interfere com elas.
_public_dir = os.path.join(os.path.dirname(__file__), "..", "public")
if os.path.isdir(_public_dir):
    from fastapi.staticfiles import StaticFiles
    app.mount("/", StaticFiles(directory=_public_dir, html=True), name="static")
