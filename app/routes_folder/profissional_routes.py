from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.models.profissional import Profissional
from app.schemas.profissional import ProfissionalCreate, ProfissionalUpdate, ProfissionalOut
from app.database import get_db
from app.dependencies import get_current_user

router = APIRouter()

@router.get("/", response_model=List[ProfissionalOut])
def listar_profissionais(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return db.query(Profissional).all()

@router.post("/", response_model=ProfissionalOut)
def criar_profissional(profissional: ProfissionalCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_prof = Profissional(**profissional.dict())
    db.add(db_prof)
    db.commit()
    db.refresh(db_prof)
    return db_prof

@router.get("/{profissional_id}", response_model=ProfissionalOut)
def obter_profissional(profissional_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    prof = db.query(Profissional).filter(Profissional.id == profissional_id).first()
    if not prof:
        raise HTTPException(status_code=404, detail="Profissional não encontrado.")
    return prof

@router.put("/{profissional_id}", response_model=ProfissionalOut)
def atualizar_profissional(
    profissional_id: int,
    profissional_update: ProfissionalUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    db_prof = db.query(Profissional).filter(Profissional.id == profissional_id).first()
    if not db_prof:
        raise HTTPException(status_code=404, detail="Profissional não encontrado.")
    
    for key, value in profissional_update.dict(exclude_unset=True).items():
        setattr(db_prof, key, value)
    
    db.commit()
    db.refresh(db_prof)
    return db_prof

@router.delete("/{profissional_id}")
def deletar_profissional(
    profissional_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    db_prof = db.query(Profissional).filter(Profissional.id == profissional_id).first()
    if not db_prof:
        raise HTTPException(status_code=404, detail="Profissional não encontrado.")
    
    db.delete(db_prof)
    db.commit()
    
    return {"message": "Profissional removido com sucesso"}
