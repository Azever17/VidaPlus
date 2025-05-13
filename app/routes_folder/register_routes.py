from fastapi import APIRouter, HTTPException
from app.schemas.auth import RegisterRequest
from app.models.usuario import Usuario
from app.database import SessionLocal
from app.auth.jwt import hash_password

router = APIRouter()


@router.post("/register")
def register_user(request: RegisterRequest):
    # Consultar se o usuário já existe
    db: SessionLocal = SessionLocal()
    user = db.query(Usuario).filter(Usuario.username == request.username).first()

    if user:
        db.close()
        raise HTTPException(status_code=400, detail="Usuário já existe")

    # Criar um novo usuário com senha criptografada
    hashed_password = hash_password(request.password)
    new_user = Usuario(username=request.username, password=hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()

    return {"message": "Usuário criado com sucesso!"}
