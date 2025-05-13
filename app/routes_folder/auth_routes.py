from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.auth.jwt import create_access_token, verify_password
from app.schemas.auth import LoginRequest, Token
from app.database import get_db
from app.models.usuario import UsuarioORM

router = APIRouter()

@router.post("/token", response_model=Token)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    print(f"\n=== Tentativa de login ===")
    print(f"Username: {request.username}")
    
    user = db.query(UsuarioORM).filter(UsuarioORM.username == request.username).first()
    
    if not user:
        print(f"Usuário não encontrado: {request.username}")
        raise HTTPException(status_code=400, detail="Usuário ou senha incorretos")
    
    print(f"Usuário encontrado: {user.username}")
    print(f"Hash armazenado: {user.hashed_password}")
    
    if not verify_password(request.password, user.hashed_password):
        print(f"Senha incorreta para usuário: {request.username}")
        raise HTTPException(status_code=400, detail="Usuário ou senha incorretos")

    print("Senha verificada com sucesso!")
    access_token = create_access_token(data={"sub": str(user.id)})
    print(f"Token gerado com sucesso para usuário: {request.username}")
    print("=== Login concluído ===\n")
    
    return Token(access_token=access_token, token_type="bearer")
