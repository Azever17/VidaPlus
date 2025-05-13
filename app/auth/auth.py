from app.models.usuario import Usuario
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.auth.jwt import verify_token
from app.db.db import SessionLocal

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

# Função para autenticar o usuário com token JWT
def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload
