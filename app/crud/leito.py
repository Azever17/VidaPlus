from sqlalchemy.orm import Session

from app.models.leito import Leito
from app.schemas.leito import LeitoCreate


def criar_leito(db: Session, leito: LeitoCreate):
    db_leito = Leito(**leito.model_dump())
    db.add(db_leito)
    db.commit()
    db.refresh(db_leito)
    return db_leito

def listar_leitos(db: Session):
    return db.query(Leito).all()

def obter_leito(db: Session, leito_id: int):
    return db.query(Leito).filter(Leito.id == leito_id).first()

def atualizar_ocupacao(db: Session, leito_id: int, ocupado: bool):
    leito = db.query(Leito).filter(Leito.id == leito_id).first()
    if leito:
        leito.ocupado = ocupado
        db.commit()
        db.refresh(leito)
    return leito
