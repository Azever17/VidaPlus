from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models.internacao import Internacao as InternacaoModel
from app.schemas.internacao import InternacaoCreate, InternacaoOut
from app.dependencies import get_current_user, get_db

router = APIRouter()

@router.get("/", response_model=List[InternacaoOut])
def listar_internacoes(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return db.query(InternacaoModel).all()

@router.post("/", response_model=InternacaoOut)
def criar_internacao(internacao: InternacaoCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_internacao = InternacaoModel(**internacao.dict())
    db.add(db_internacao)
    db.commit()
    db.refresh(db_internacao)
    return db_internacao
