"""
COD-IV — Script de seed da base de dados.

Corre uma vez (localmente ou via `python seed_db.py`) para popular:
  1. Tabela `sinais`            <- data/sinais.json
  2. Tabela `perguntas_mecanica` <- data/mecanica.json
  3. Tabela `quiz_perguntas` + `quiz_opcoes`, Tipo C (reconhecimento de
     sinais): gerado automaticamente aqui, sem precisar de curadoria manual.

NOTA: As perguntas Tipo A (afirmações com imagem, mecânica) e Tipo B
(afirmações sem imagem, código+mecânica) dependem de um banco de afirmações
erradas plausíveis, que precisa de validação de qualidade antes da geração
em massa (ver docs/COD-IV_briefing.md, secção 7). Ficam marcadas como TODO
abaixo — a preencher depois do lote de teste ser aprovado.
"""
import json
import random
from pathlib import Path

from api.database import Base, engine, SessionLocal
from api import models

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def carregar_json(nome_ficheiro):
    caminho = DATA_DIR / nome_ficheiro
    with open(caminho, encoding="utf-8") as f:
        return json.load(f)


def seed_sinais(db):
    sinais_data = carregar_json("sinais.json")
    if db.query(models.Sinal).count() > 0:
        print("Tabela 'sinais' já tem dados — a saltar.")
        return db.query(models.Sinal).all()

    objetos = []
    for s in sinais_data:
        objetos.append(models.Sinal(
            codigo=s["codigo"],
            nome=s["nome"],
            categoria=s["categoria"],
            subcategoria=s.get("subcategoria"),
            imagem_url=s.get("imagem_url"),
            descricao=s.get("descricao"),
        ))
    db.add_all(objetos)
    db.commit()
    print(f"Inseridos {len(objetos)} sinais.")
    return db.query(models.Sinal).all()


def seed_mecanica(db):
    mecanica_data = carregar_json("mecanica.json")
    if db.query(models.PerguntaMecanica).count() > 0:
        print("Tabela 'perguntas_mecanica' já tem dados — a saltar.")
        return db.query(models.PerguntaMecanica).all()

    objetos = []
    for p in mecanica_data:
        objetos.append(models.PerguntaMecanica(
            pergunta=p["pergunta"],
            resposta_correta=p["resposta_correta"],
            categoria=p["categoria"],
            imagem_url=p.get("imagem_url"),
        ))
    db.add_all(objetos)
    db.commit()
    print(f"Inseridas {len(objetos)} perguntas de mecânica.")
    return db.query(models.PerguntaMecanica).all()


def gerar_perguntas_reconhecimento(db, sinais):
    """
    Tipo C: imagem do sinal + 4 nomes possíveis (1 certo + 3 distratores
    da mesma categoria, para não ficarem óbvios demais).
    """
    if db.query(models.QuizPergunta).filter_by(tipo="reconhecimento").count() > 0:
        print("Perguntas Tipo C já existem — a saltar.")
        return

    por_categoria = {}
    for s in sinais:
        por_categoria.setdefault(s.categoria, []).append(s)

    total_criadas = 0
    for sinal in sinais:
        mesma_categoria = [
            s for s in por_categoria[sinal.categoria] if s.id != sinal.id
        ]
        if len(mesma_categoria) < 3:
            # categoria pequena demais para 3 distratores só dela — completa com o resto
            outros = [s for s in sinais if s.id != sinal.id and s not in mesma_categoria]
            distratores_pool = mesma_categoria + outros
        else:
            distratores_pool = mesma_categoria

        distratores = random.sample(distratores_pool, k=min(3, len(distratores_pool)))

        pergunta = models.QuizPergunta(
            tipo="reconhecimento",
            materia="codigo",
            categoria=sinal.categoria,
            enunciado="Que sinal é este?",
            imagem_url=sinal.imagem_url,
            referencia_id=sinal.id,
        )
        db.add(pergunta)
        db.flush()  # garante pergunta.id antes de criar as opções

        opcoes = [(sinal.nome, True)] + [(d.nome, False) for d in distratores]
        random.shuffle(opcoes)

        for ordem, (texto, correta) in enumerate(opcoes):
            db.add(models.QuizOpcao(
                pergunta_id=pergunta.id,
                texto=texto,
                correta=correta,
                ordem=ordem,
            ))
        total_criadas += 1

    db.commit()
    print(f"Geradas {total_criadas} perguntas Tipo C (reconhecimento).")


# Rótulos legíveis para as categorias de sinais (usados nas afirmações
# Tipo B). Categoria não mapeada aqui cai no fallback (underscores -> espaços).
CATEGORIA_SINAL_LABEL = {
    "sinais_perigo": "sinais de perigo",
    "sinais_cedencia_passagem": "sinais de cedência de passagem",
    "sinais_proibicao": "sinais de proibição",
    "sinais_obrigacao": "sinais de obrigação",
    "sinais_seleccao_vias": "sinais de seleção de vias",
    "sinais_afectacao_vias": "sinais de afetação de vias",
    "sinais_zona": "sinais de zona",
    "sinais_informacao": "sinais de informação",
    "sinais_pre_sinalizacao": "sinais de pré-sinalização",
    "sinais_direccao": "sinais de direção",
    "sinais_confirmacao": "sinais de confirmação",
    "sinais_identificacao_localidades": "sinais de identificação de localidades",
    "sinais_complementares": "sinais complementares",
    "sinalizacao_turistico_cultural": "sinalização turístico-cultural",
    "marcas_rodoviarias": "marcas rodoviárias",
    "sinalizacao_temporaria": "sinalização temporária",
    "dispositivos_complementares": "dispositivos complementares",
    "simbolos_apoio_utente": "símbolos de apoio ao utente",
    "simbolos_turisticos": "símbolos turísticos",
    "simbolos_geograficos_ecologicos": "símbolos geográficos/ecológicos",
    "simbolos_culturais": "símbolos culturais",
    "simbolos_desportivos": "símbolos desportivos",
    "simbolos_industriais": "símbolos industriais",
}


def _label_categoria_sinal(categoria: str) -> str:
    return CATEGORIA_SINAL_LABEL.get(categoria, categoria.replace("_", " "))


def _pergunta_para_afirmacao(pergunta: str, resposta: str) -> str:
    """
    Converte um par pergunta/resposta do manual de mecânica numa frase de
    afirmação para o formato "3 afirmações" (Tipo B).

    NOTA DE DESIGN: em vez de tentar reescrever a resposta em português
    "perfeito" por regras (arriscado — o manual tem dezenas de padrões de
    pergunta diferentes e uma reescrita mal feita pode introduzir erros
    factuais ou frases estranhas), mantemos o enunciado no formato
    "Tópico: conteúdo do manual", que é honesto sobre a origem do texto e
    evita qualquer distorção do conteúdo original.
    """
    topico = pergunta.strip().rstrip("?").strip()
    # Deixa a primeira letra do tópico em minúscula quando começa por
    # "O que é / Para que serve" etc., para ler melhor como afirmação.
    return f"{topico}: {resposta.strip()}"


def gerar_perguntas_afirmacoes_codigo(db, sinais, n_por_grupo=3):
    """
    Tipo B — Código: 3 afirmações sobre a categoria de sinais de trânsito
    (2 certas, 1 errada). Gera 1 pergunta por sinal, usando esse sinal como
    a afirmação errada (atribuída a uma categoria que não é a sua) e 2
    outros sinais aleatórios como afirmações corretas.
    """
    if db.query(models.QuizPergunta).filter_by(tipo="afirmacoes", materia="codigo").count() > 0:
        print("Perguntas Tipo B (código) já existem — a saltar.")
        return

    categorias = sorted({s.categoria for s in sinais})
    if len(categorias) < 2 or len(sinais) < n_por_grupo:
        print("Dados insuficientes para gerar Tipo B (código).")
        return

    total_criadas = 0
    for sinal_errado in sinais:
        outros = [s for s in sinais if s.id != sinal_errado.id]
        certos = random.sample(outros, k=n_por_grupo - 1)

        categoria_falsa = random.choice([c for c in categorias if c != sinal_errado.categoria])

        afirmacoes = [
            (f"O sinal \u201c{s.nome}\u201d pertence à categoria de {_label_categoria_sinal(s.categoria)}.", True)
            for s in certos
        ]
        afirmacoes.append((
            f"O sinal \u201c{sinal_errado.nome}\u201d pertence à categoria de {_label_categoria_sinal(categoria_falsa)}.",
            False,
        ))
        random.shuffle(afirmacoes)

        pergunta = models.QuizPergunta(
            tipo="afirmacoes",
            materia="codigo",
            categoria=sinal_errado.categoria,
            enunciado="Destas afirmações sobre sinalização rodoviária, quais estão corretas?",
            imagem_url=None,
            referencia_id=sinal_errado.id,
        )
        db.add(pergunta)
        db.flush()

        for ordem, (texto, correta) in enumerate(afirmacoes):
            db.add(models.QuizOpcao(pergunta_id=pergunta.id, texto=texto, correta=correta, ordem=ordem))
        total_criadas += 1

    db.commit()
    print(f"Geradas {total_criadas} perguntas Tipo B (código).")


def gerar_perguntas_afirmacoes_mecanica(db, perguntas_mecanica, n_por_grupo=3):
    """
    Tipo B — Mecânica: 3 afirmações (2 certas, 1 errada). A afirmação errada
    junta o enunciado de uma pergunta real a uma resposta de OUTRA pergunta
    da mesma categoria (troca de par pergunta/resposta) — continua a ser
    conteúdo genuíno do manual, só que mal associado, o que produz um
    distrator plausível sem inventar factos novos.
    """
    if db.query(models.QuizPergunta).filter_by(tipo="afirmacoes", materia="mecanica").count() > 0:
        print("Perguntas Tipo B (mecânica) já existem — a saltar.")
        return

    por_categoria = {}
    for p in perguntas_mecanica:
        por_categoria.setdefault(p.categoria, []).append(p)

    total_criadas = 0
    for p_errada in perguntas_mecanica:
        pool_categoria = [p for p in por_categoria[p_errada.categoria] if p.id != p_errada.id]
        if len(pool_categoria) < n_por_grupo:
            # categoria pequena demais — completa com o resto do banco
            pool_categoria = [p for p in perguntas_mecanica if p.id != p_errada.id]
        if len(pool_categoria) < n_por_grupo:
            continue

        certos = random.sample(pool_categoria, k=n_por_grupo - 1)
        # resposta errada: de outra pergunta da mesma categoria, garantindo
        # que não coincide por acaso com a resposta certa de p_errada
        candidatos_resposta_falsa = [
            p for p in pool_categoria if p.resposta_correta != p_errada.resposta_correta
        ]
        if not candidatos_resposta_falsa:
            continue
        resposta_falsa = random.choice(candidatos_resposta_falsa).resposta_correta

        afirmacoes = [(_pergunta_para_afirmacao(p.pergunta, p.resposta_correta), True) for p in certos]
        afirmacoes.append((_pergunta_para_afirmacao(p_errada.pergunta, resposta_falsa), False))
        random.shuffle(afirmacoes)

        pergunta = models.QuizPergunta(
            tipo="afirmacoes",
            materia="mecanica",
            categoria=p_errada.categoria,
            enunciado="Destas afirmações sobre mecânica automóvel, quais estão corretas?",
            imagem_url=None,
            referencia_id=p_errada.id,
        )
        db.add(pergunta)
        db.flush()

        for ordem, (texto, correta) in enumerate(afirmacoes):
            db.add(models.QuizOpcao(pergunta_id=pergunta.id, texto=texto, correta=correta, ordem=ordem))
        total_criadas += 1

    db.commit()
    print(f"Geradas {total_criadas} perguntas Tipo B (mecânica).")


def gerar_perguntas_afirmacoes_imagem_mecanica(db, perguntas_mecanica, n_opcoes=4):
    """
    Tipo A — Mecânica: imagem da peça + 4 afirmações (3 certas, 1 errada).

    BLOQUEADO: nenhuma entrada de perguntas_mecanica tem imagem_url
    preenchido ainda (0 de 202 no ficheiro atual) — falta o Danilo fornecer
    as imagens das peças. Esta função já está pronta: assim que as imagens
    forem adicionadas a data/mecanica.json (campo "imagem_url") e o seed
    correr de novo, as perguntas Tipo A são geradas automaticamente com a
    mesma lógica de distratores por categoria do Tipo B.
    """
    com_imagem = [p for p in perguntas_mecanica if p.imagem_url]
    if not com_imagem:
        print("Tipo A (mecânica): 0 perguntas com imagem — pendente de imagens do Danilo, a saltar.")
        return

    if db.query(models.QuizPergunta).filter_by(tipo="afirmacoes_imagem").count() > 0:
        print("Perguntas Tipo A já existem — a saltar.")
        return

    por_categoria = {}
    for p in perguntas_mecanica:
        por_categoria.setdefault(p.categoria, []).append(p)

    total_criadas = 0
    for p_base in com_imagem:
        pool_categoria = [p for p in por_categoria[p_base.categoria] if p.id != p_base.id]
        if len(pool_categoria) < n_opcoes - 1:
            pool_categoria = [p for p in perguntas_mecanica if p.id != p_base.id]
        if len(pool_categoria) < n_opcoes - 1:
            continue

        certos = random.sample(pool_categoria, k=n_opcoes - 2)
        candidatos_resposta_falsa = [p for p in pool_categoria if p.resposta_correta != p_base.resposta_correta]
        if not candidatos_resposta_falsa:
            continue
        resposta_falsa = random.choice(candidatos_resposta_falsa).resposta_correta

        afirmacoes = [(_pergunta_para_afirmacao(p_base.pergunta, p_base.resposta_correta), True)]
        afirmacoes += [(_pergunta_para_afirmacao(p.pergunta, p.resposta_correta), True) for p in certos]
        afirmacoes.append((_pergunta_para_afirmacao(p_base.pergunta, resposta_falsa), False))
        random.shuffle(afirmacoes)

        pergunta = models.QuizPergunta(
            tipo="afirmacoes_imagem",
            materia="mecanica",
            categoria=p_base.categoria,
            enunciado="Sobre esta peça, quais afirmações estão corretas?",
            imagem_url=p_base.imagem_url,
            referencia_id=p_base.id,
        )
        db.add(pergunta)
        db.flush()

        for ordem, (texto, correta) in enumerate(afirmacoes):
            db.add(models.QuizOpcao(pergunta_id=pergunta.id, texto=texto, correta=correta, ordem=ordem))
        total_criadas += 1

    db.commit()
    print(f"Geradas {total_criadas} perguntas Tipo A (mecânica, com imagem).")


def main():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        sinais = seed_sinais(db)
        perguntas_mecanica = seed_mecanica(db)
        gerar_perguntas_reconhecimento(db, sinais)          # Tipo C — código
        gerar_perguntas_afirmacoes_codigo(db, sinais)        # Tipo B — código
        gerar_perguntas_afirmacoes_mecanica(db, perguntas_mecanica)  # Tipo B — mecânica
        gerar_perguntas_afirmacoes_imagem_mecanica(db, perguntas_mecanica)  # Tipo A — mecânica (pendente de imagens)
    finally:
        db.close()


if __name__ == "__main__":
    main()
