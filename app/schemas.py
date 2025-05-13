from pydantic import BaseModel
from typing import Optional
from datetime import date

class PacienteBase(BaseModel):
    nome: str
    cpf: str
    data_nascimento: date
    email: str
    telefone: str

class PacienteCreate(PacienteBase):
    pass

class PacienteUpdate(BaseModel):
    nome: Optional[str] = None
    cpf: Optional[str] = None
    data_nascimento: Optional[date] = None
    email: Optional[str] = None
    telefone: Optional[str] = None

class Paciente(PacienteBase):
    id: int

    class Config:
        from_attributes = True

class PacienteOut(PacienteBase):
    id: int

    class Config:
        from_attributes = True

