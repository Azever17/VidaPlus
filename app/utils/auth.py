from fastapi import Depends, HTTPException, Header
from app.auth.jwt import verificar_token

def get_current_user(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token inválido")

    token = authorization.split(" ")[1]
    user_id = verificar_token(token)

    if user_id is None:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")

    for user in usuarios_fake_db:
        if user.id == user_id:
            return user

    raise HTTPException(status_code=404, detail="Usuário não encontrado")
