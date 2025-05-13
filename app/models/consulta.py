import enum
from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

class Consulta(Base):
    __tablename__ = "consultas"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, nullable=False)
    profissional_id = Column(Integer, nullable=False)
    data_hora = Column(DateTime)
    tipo = Column(String, nullable=False)

class StatusConsulta(str, enum.Enum):
    AGENDADA = "agendada"
    REALIZADA = "realizada"
    CANCELADA = "cancelada"

class TipoConsulta(str, enum.Enum):
    PRESENCIAL = "presencial"
    ONLINE = "online"