from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models.paciente import Paciente as PacienteModel
from app.schemas.paciente import PacienteCreate, PacienteUpdate, PacienteOut
from app.dependencies import get_current_user, get_db

router = APIRouter()

@router.get("/", response_model=List[PacienteOut])
def listar_pacientes(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return db.query(PacienteModel).all()

@router.post("/", response_model=PacienteOut)
def criar_paciente(
    paciente: PacienteCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    db_paciente = PacienteModel(**paciente.dict())
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

@router.get("/{paciente_id}", response_model=PacienteOut)
def obter_paciente(
    paciente_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    paciente = db.query(PacienteModel).filter(PacienteModel.id == paciente_id).first()
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado.")
    return paciente

@router.put("/{paciente_id}", response_model=PacienteOut)
def atualizar_paciente(
    paciente_id: int,
    paciente_update: PacienteUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    db_paciente = db.query(PacienteModel).filter(PacienteModel.id == paciente_id).first()
    if not db_paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado.")
    
    for key, value in paciente_update.dict(exclude_unset=True).items():
        setattr(db_paciente, key, value)
    
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

@router.delete("/{paciente_id}")
def deletar_paciente(
    paciente_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    db_paciente = db.query(PacienteModel).filter(PacienteModel.id == paciente_id).first()
    if not db_paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado.")
    
    db.delete(db_paciente)
    db.commit()
    
    return {"message": "Paciente removido com sucesso"}
