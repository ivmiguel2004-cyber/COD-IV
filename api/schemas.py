"""
COD-IV — Schemas Pydantic para request/response da API.
"""
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field


# ---------- Utilizador ----------
class CadastroRequest(BaseModel):
    primeiro_nome: str = Field(..., min_length=1, max_length=80)
    ultimo_nome: str = Field(..., min_length=1, max_length=80)
    password: str = Field(..., min_length=6, max_length=100)


class LoginRequest(BaseModel):
    primeiro_nome: str
    ultimo_nome: str
    password: str


class UtilizadorOut(BaseModel):
    id: int
    primeiro_nome: str
    ultimo_nome: str

    class Config:
        from_attributes = True


class AuthResponse(BaseModel):
    token: str
    utilizador: UtilizadorOut


# ---------- Quiz — iniciar sessão ----------
class IniciarQuizRequest(BaseModel):
    materia: str = Field(..., pattern="^(codigo|mecanica)$")
    num_perguntas: int = Field(..., description="10, 15, 20 ou 50")


class OpcaoOut(BaseModel):
    id: int
    texto: str
    ordem: int

    class Config:
        from_attributes = True


class PerguntaOut(BaseModel):
    id: int
    tipo: str
    materia: str
    categoria: Optional[str]
    enunciado: Optional[str]
    imagem_url: Optional[str]
    opcoes: List[OpcaoOut]

    class Config:
        from_attributes = True


class QuizSessionOut(BaseModel):
    id: int
    materia: str
    num_perguntas: int
    tempo_total_segundos: int
    iniciado_em: datetime
    perguntas: List[PerguntaOut]

    class Config:
        from_attributes = True


# ---------- Quiz — responder ----------
class ResponderPerguntaRequest(BaseModel):
    pergunta_id: int
    opcoes_escolhidas: List[int] = Field(default_factory=list)
    saltada: bool = False


# ---------- Quiz — resultados ----------
class RespostaResultadoOut(BaseModel):
    pergunta_id: int
    enunciado: Optional[str]
    imagem_url: Optional[str]
    opcoes: List[OpcaoOut]
    opcoes_corretas_ids: List[int]
    opcoes_escolhidas_ids: List[int]
    correta: bool
    saltada: bool


class ResultadoQuizOut(BaseModel):
    quiz_session_id: int
    materia: str
    total_perguntas: int
    total_certas: int
    total_erradas: int
    respostas: List[RespostaResultadoOut]
