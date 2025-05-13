from sqlalchemy import Column, Integer, String, Date
from app.database import Base


class Paciente(Base):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    idade = Column(Integer)
    sexo = Column(String)
    endereco = Column(String)
    email = Column(String)
    data_nascimento = Column(Date, nullable=True)
