"""
COD-IV — Ligação à base de dados.

Lê a variável de ambiente DATABASE_URL (definida no Vercel quando ligares o
Postgres/Neon). Em desenvolvimento local, se DATABASE_URL não existir, cai
para um ficheiro SQLite local (cod_iv_dev.db) para facilitar testes sem
precisar de um Postgres a correr.
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import NullPool

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL:
    # Postgres (produção — Vercel/Neon)
    # Neon costuma dar URLs "postgres://"; SQLAlchemy quer "postgresql://"
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

    # CORREÇÃO: em funções serverless (Vercel), cada invocação pode correr
    # num processo/container novo. Um pool normal (QueuePool) mantém ligações
    # "penduradas" entre invocações e esgota rapidamente o limite de ligações
    # do Neon (free tier tem poucas dezenas). NullPool fecha a ligação no fim
    # de cada pedido — mais lento por pedido, mas seguro em serverless.
    # IMPORTANTE: usa a connection string "pooled" do Neon (com "-pooler" no
    # host, via PgBouncer) na env var DATABASE_URL, para amortizar o custo de
    # abrir ligação a cada pedido.
    engine = create_engine(DATABASE_URL, poolclass=NullPool, pool_pre_ping=True)
else:
    # Desenvolvimento local
    engine = create_engine(
        "sqlite:///./cod_iv_dev.db",
        connect_args={"check_same_thread": False},
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """Dependency do FastAPI: abre e fecha a sessão da BD por pedido."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
