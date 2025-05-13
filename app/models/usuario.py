from pydantic import BaseModel
from enum import Enum
from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base  # Certifique-se de que a Base está sendo importada corretamente

class UsuarioORM(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    tipo_usuario = Column(String)
    ativo = Column(Boolean, default=True)

class TipoUsuario(str, Enum):
    ADMIN = "admin"
    MEDICO = "medico"
    ENFERMEIRO = "enfermeiro"
    PACIENTE = "paciente"

class UsuarioCreate(BaseModel):  # Renomeado para evitar conflito
    id: int
    nome: str
    email: str
    senha: str
    tipo_usuario: TipoUsuario

    class Config:
        from_attributes = True  # Não se esqueça de manter esse flag para permitir a conversão de modelos
