"""
COD-IV — Lógica de geração e avaliação de sessões de quiz.
"""
import random
from typing import List
from sqlalchemy.orm import Session, joinedload

import models

NUM_PERGUNTAS_VALIDOS = (10, 15, 20, 50)
TEMPO_POR_PERGUNTA_SEGUNDOS = 90  # 1,5 min por pergunta


def validar_num_perguntas(num: int) -> int:
    if num not in NUM_PERGUNTAS_VALIDOS:
        raise ValueError(f"Número de perguntas inválido. Escolhe entre {NUM_PERGUNTAS_VALIDOS}.")
    return num


def calcular_tempo_total(num_perguntas: int) -> int:
    return num_perguntas * TEMPO_POR_PERGUNTA_SEGUNDOS


def selecionar_perguntas(db: Session, materia: str, num_perguntas: int) -> List[models.QuizPergunta]:
    """
    Escolhe aleatoriamente `num_perguntas` perguntas da matéria pedida,
    já com as opções carregadas (evita N+1 queries).
    """
    disponiveis = (
        db.query(models.QuizPergunta)
        .options(joinedload(models.QuizPergunta.opcoes))
        .filter(models.QuizPergunta.materia == materia)
        .all()
    )
    if len(disponiveis) < num_perguntas:
        raise ValueError(
            f"Só há {len(disponiveis)} perguntas disponíveis para '{materia}', "
            f"pedidas {num_perguntas}. É preciso gerar mais perguntas nesta matéria."
        )
    return random.sample(disponiveis, num_perguntas)


def avaliar_resposta(pergunta: models.QuizPergunta, opcoes_escolhidas_ids: List[int]) -> bool:
    """
    Regra de pontuação: a pergunta só conta como certa se o conjunto de
    opções escolhidas for exatamente igual ao conjunto de opções corretas
    (nem falta nenhuma certa, nem sobra nenhuma errada).
    """
    corretas_ids = {o.id for o in pergunta.opcoes if o.correta}
    escolhidas_ids = set(opcoes_escolhidas_ids)
    return corretas_ids == escolhidas_ids
