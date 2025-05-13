# app/crud/consulta_crud.py

from sqlalchemy.orm import Session
from app.models.consulta import Consulta
from app.schemas.consulta import ConsultaCreate

def criar_consulta(db: Session, dados: ConsultaCreate):
    nova_consulta = Consulta(**dados.dict())
    db.add(nova_consulta)
    db.commit()
    db.refresh(nova_consulta)
    return nova_consulta

def cancelar_consulta(db: Session, consulta_id: int):
    consulta = db.query(Consulta).get(consulta_id)
    if consulta:
        consulta.status = "Cancelada"
        db.commit()
    return consulta
