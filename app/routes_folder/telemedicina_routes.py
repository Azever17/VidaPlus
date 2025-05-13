# app/routes/telemedicina_routes.py
from fastapi import APIRouter, Depends
from app.database import SessionLocal
from app.models import Consulta
from sqlalchemy.orm import Session

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/consulta")
def iniciar_consulta(medico_id: int, paciente_id: int, db: Session = Depends(get_db)):
    # Criar uma nova consulta
    consulta = Consulta(medico_id=medico_id, paciente_id=paciente_id)
    db.add(consulta)
    db.commit()

    return {"message": "Consulta iniciada com sucesso!"}
