"""
COD-IV — Modelos SQLAlchemy, espelhando o schema em sql/schema.sql
"""
from sqlalchemy import (
    Column, Integer, String, Text, Boolean, DateTime, ForeignKey, JSON
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class Utilizador(Base):
    __tablename__ = "utilizadores"

    id = Column(Integer, primary_key=True, index=True)
    primeiro_nome = Column(String(80), nullable=False)
    ultimo_nome = Column(String(80), nullable=False)
    username = Column(String(120), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    criado_em = Column(DateTime, server_default=func.now())

    sessions = relationship("QuizSession", back_populates="utilizador")


class Sinal(Base):
    __tablename__ = "sinais"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(20), nullable=False)
    nome = Column(String(200), nullable=False)
    categoria = Column(String(80), nullable=False, index=True)
    subcategoria = Column(String(80))
    imagem_url = Column(String(255))
    descricao = Column(Text)


class PerguntaMecanica(Base):
    __tablename__ = "perguntas_mecanica"

    id = Column(Integer, primary_key=True, index=True)
    pergunta = Column(Text, nullable=False)
    resposta_correta = Column(Text, nullable=False)
    categoria = Column(String(80), nullable=False, index=True)
    imagem_url = Column(String(255))


class QuizPergunta(Base):
    __tablename__ = "quiz_perguntas"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String(30), nullable=False)  # reconhecimento | afirmacoes_imagem | afirmacoes
    materia = Column(String(20), nullable=False)  # codigo | mecanica
    categoria = Column(String(80))
    enunciado = Column(Text)
    imagem_url = Column(String(255))
    referencia_id = Column(Integer)

    opcoes = relationship("QuizOpcao", back_populates="pergunta", cascade="all, delete-orphan")


class QuizOpcao(Base):
    __tablename__ = "quiz_opcoes"

    id = Column(Integer, primary_key=True, index=True)
    pergunta_id = Column(Integer, ForeignKey("quiz_perguntas.id", ondelete="CASCADE"), nullable=False)
    texto = Column(Text, nullable=False)
    correta = Column(Boolean, nullable=False, default=False)
    ordem = Column(Integer, default=0)

    pergunta = relationship("QuizPergunta", back_populates="opcoes")


class QuizSession(Base):
    __tablename__ = "quiz_sessions"

    id = Column(Integer, primary_key=True, index=True)
    utilizador_id = Column(Integer, ForeignKey("utilizadores.id", ondelete="CASCADE"), nullable=False)
    materia = Column(String(20), nullable=False)
    num_perguntas = Column(Integer, nullable=False)
    tempo_total_segundos = Column(Integer, nullable=False)
    iniciado_em = Column(DateTime, server_default=func.now())
    finalizado_em = Column(DateTime, nullable=True)
    status = Column(String(20), nullable=False, default="em_progresso")

    utilizador = relationship("Utilizador", back_populates="sessions")
    respostas = relationship("QuizResposta", back_populates="session", cascade="all, delete-orphan")


class QuizResposta(Base):
    __tablename__ = "quiz_respostas"

    id = Column(Integer, primary_key=True, index=True)
    quiz_session_id = Column(Integer, ForeignKey("quiz_sessions.id", ondelete="CASCADE"), nullable=False)
    pergunta_id = Column(Integer, ForeignKey("quiz_perguntas.id"), nullable=False)
    ordem = Column(Integer, nullable=False)
    opcoes_escolhidas = Column(JSON, default=list)  # lista de ids de quiz_opcoes
    correta = Column(Boolean, nullable=True)
    saltada = Column(Boolean, nullable=False, default=False)
    respondida_em = Column(DateTime, nullable=True)

    session = relationship("QuizSession", back_populates="respostas")
