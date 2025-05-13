from sqlalchemy.orm import Session
from app.models.hospital import Hospital
from app.schemas.hospital import HospitalCreate

def criar_hospital(db: Session, hospital: HospitalCreate):
    db_hospital = Hospital(**hospital.model_dump())
    db.add(db_hospital)
    db.commit()
    db.refresh(db_hospital)
    return db_hospital

def listar_hospitais(db: Session):
    return db.query(Hospital).all()

def obter_hospital(db: Session, hospital_id: int):
    return db.query(Hospital).filter(Hospital.id == hospital_id).first()
