from sqlalchemy import Column, Integer, ForeignKey, Date, String
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.paciente import Paciente
from app.models.leito import Leito

class Internacao(Base):
    __tablename__ = "internacoes"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"))
    leito_id = Column(Integer, ForeignKey("leitos.id"))
    data_entrada = Column(Date)
    data_alta = Column(Date, nullable=True)
    motivo = Column(String)

    paciente = relationship(Paciente)  # Definindo o relacionamento com Paciente
    leito = relationship(Leito)  # Definindo o relacionamento com Leito