"""
COD-IV — Autenticação.

- Password: hash com bcrypt (passlib).
- Username interno: gerado a partir do nome + sufixo aleatório, garante
  unicidade mesmo com nomes repetidos. Nunca é mostrado ao utilizador.
- Sessão: token JWT simples (assinado com SECRET_KEY), sem necessidade de
  guardar sessões em BD.
"""
import os
import re
import secrets
import unicodedata
from datetime import datetime, timedelta, timezone

import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from api import models

SECRET_KEY = os.environ.get("COD_IV_SECRET_KEY", "muda-esta-chave-em-producao")
ALGORITHM = "HS256"
TOKEN_EXPIRE_HOURS = 12

# CORREÇÃO: impede arrancar em produção (Vercel define VERCEL_ENV) sem a
# variável COD_IV_SECRET_KEY definida — evita assinar tokens com uma chave
# previsível e pública (estava neste ficheiro em texto simples).
if os.environ.get("VERCEL_ENV") == "production" and SECRET_KEY == "muda-esta-chave-em-producao":
    raise RuntimeError(
        "COD_IV_SECRET_KEY não está definida em produção. "
        "Define-a nas Environment Variables do projeto no Vercel "
        "(usa por exemplo: python -c \"import secrets; print(secrets.token_hex(32))\")."
    )

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    return pwd_context.verify(password, password_hash)


def _slugify(texto: str) -> str:
    """Remove acentos e caracteres especiais, devolve minúsculas com hífens."""
    texto_normalizado = unicodedata.normalize("NFKD", texto)
    sem_acentos = "".join(c for c in texto_normalizado if not unicodedata.combining(c))
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", sem_acentos).strip("-").lower()
    return slug or "utilizador"


def gerar_username_unico(db: Session, primeiro_nome: str, ultimo_nome: str) -> str:
    """
    Gera um username interno único (ex: 'ivandro-miguel-a91f').
    Nunca é mostrado ao utilizador — serve só de chave interna.
    """
    base = _slugify(f"{primeiro_nome}-{ultimo_nome}")
    while True:
        candidato = f"{base}-{secrets.token_hex(2)}"
        existe = db.query(models.Utilizador).filter_by(username=candidato).first()
        if not existe:
            return candidato


def criar_token(utilizador_id: int) -> str:
    payload = {
        "sub": str(utilizador_id),
        "exp": datetime.now(timezone.utc) + timedelta(hours=TOKEN_EXPIRE_HOURS),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def validar_token(token: str) -> int:
    """Devolve o id do utilizador se o token for válido, senão levanta erro."""
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return int(payload["sub"])
