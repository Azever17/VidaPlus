from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models.leito import Leito as LeitoModel
from app.schemas.leito import LeitoCreate, LeitoOut
from app.dependencies import get_current_user, get_db

router = APIRouter()

@router.get("/", response_model=List[LeitoOut])
def listar_leitos(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return db.query(LeitoModel).all()

@router.post("/", response_model=LeitoOut)
def criar_leito(leito: LeitoCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_leito = LeitoModel(**leito.dict())
    db.add(db_leito)
    db.commit()
    db.refresh(db_leito)
    return db_leito