from pydantic import BaseModel
from typing import Optional

# Base comum
class HospitalBase(BaseModel):
    nome: str
    endereco: Optional[str] = None
    telefone: Optional[str] = None

# Schema para criação (input)
class HospitalCreate(HospitalBase):
    nome: str
    endereco: str
    telefone: str

# Schema para resposta resumida (output)
class HospitalOut(HospitalBase):
    id: int

    class Config:
        from_attributes = True

# Schema mais completo se necessário
class HospitalResponse(HospitalOut):
    pass
