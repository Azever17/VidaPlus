from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal
from fastapi.responses import FileResponse
import os

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/agendamentos/", response_model=schemas.Agendamento)
def create_agendamento(agendamento: schemas.AgendamentoCreate, db: Session = Depends(get_db)):
    return crud.create_agendamento(db=db, agendamento=agendamento)

@router.get("/agendamentos/{agendamento_id}", response_model=schemas.Agendamento)
def read_agendamento(agendamento_id: int, db: Session = Depends(get_db)):
    db_agendamento = crud.get_agendamento(db=db, agendamento_id=agendamento_id)
    if db_agendamento is None:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")
    return db_agendamento


@router.get("/laudo/{agendamento_id}")
def download_laudo(agendamento_id: int, db: Session = Depends(get_db)):
    agendamento = db.query(Agendamento).filter(Agendamento.id == agendamento_id).first()

    if agendamento is None:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")

    if not agendamento.laudo_url:
        raise HTTPException(status_code=404, detail="Laudo não gerado ainda")

    laudo_path = agendamento.laudo_url
    return FileResponse(laudo_path, media_type="application/pdf")