from app.auth.jwt import hash_password
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.usuario import UsuarioORM
from app.schemas.usuario import UsuarioCreate, UsuarioResponse

router = APIRouter()

@router.post("/register", response_model=UsuarioResponse)
def register_user(request: UsuarioCreate, db: Session = Depends(get_db)):
    existing_user = db.query(UsuarioORM).filter(UsuarioORM.username == request.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Usuário já existe")

    new_user = UsuarioORM(
        username=request.username,
        email=request.email,
        password=request.password,
        tipo_usuario=request.tipo_usuario.value
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

    if user:
        db.close()
        raise HTTPException(status_code=400, detail="Usuário já existe")

    hashed_password = hash_password(request.password)
    new_user = Usuario(username=request.username, password=hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()

    return {"message": "Usuário criado com sucesso!"}
