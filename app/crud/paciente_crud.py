from sqlalchemy.orm import Session
from app.models.paciente import Paciente
from app.schemas.paciente import PacienteCreate, PacienteUpdate

def get_paciente(db: Session, paciente_id: int = None):
    if paciente_id:
        return db.query(Paciente).filter(Paciente.id == paciente_id).first()
    return db.query(Paciente).all()

def create_paciente(db: Session, paciente: PacienteCreate):
    db_paciente = Paciente(**paciente.dict())
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

def update_paciente(db: Session, paciente_id: int, paciente: PacienteUpdate):
    db_paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
    if db_paciente:
        for key, value in paciente.dict().items():
            setattr(db_paciente, key, value)
        db.commit()
        db.refresh(db_paciente)
    return db_paciente

def delete_paciente(db: Session, paciente_id: int):
    db_paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
    if db_paciente:
        db.delete(db_paciente)
        db.commit()
    return db_paciente
