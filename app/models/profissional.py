from sqlalchemy import Column, Integer, String, Enum
from app.database import Base
import enum

class Especialidade(str, enum.Enum):
    CLINICO = "Clínico Geral"
    PEDIATRA = "Pediatra"
    CARDIOLOGISTA = "Cardiologista"
    ORTOPEDISTA = "Ortopedista"
    DERMATOLOGISTA = "Dermatologista"

class Profissional(Base):
    __tablename__ = "profissionais"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    especialidade = Column(String)
    hospital_id = Column(Integer)
