from sqlalchemy import Column, Integer, String, Enum
from app.database import Base
import enum

class StatusLeito(str, enum.Enum):
    LIVRE = "livre"
    OCUPADO = "ocupado"
    MANUTENCAO = "manutencao"

class Leito(Base):
    __tablename__ = "leitos"

    id = Column(Integer, primary_key=True, index=True)
    numero = Column(String, unique=True, nullable=False)
    tipo = Column(String, nullable=False)  # Ex: UTI, Enfermaria, Isolamento
    status = Column(Enum(StatusLeito), default=StatusLeito.LIVRE)
    localizacao = Column(String, nullable=False)  # Ex: Ala Norte, Quarto 301
