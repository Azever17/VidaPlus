from pydantic import BaseModel
from datetime import date
from typing import Optional

class InternacaoBase(BaseModel):
    paciente_id: int
    leito_id: int
    data_internacao: date
    motivo: str

class InternacaoCreate(InternacaoBase):
    pass

class InternacaoOut(InternacaoBase):
    id: int
    data_alta: Optional[date] = None

    class Config:
        from_attributes = True
