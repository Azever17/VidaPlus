from sqlalchemy import Column, Integer, String
from app.database import Base

class Medico(Base):
    __tablename__ = "medicos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    crm = Column(String, unique=True, nullable=False)
    especialidade = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    telefone = Column(String) 