from pydantic import BaseModel
from typing import Optional
import enum

class StatusLeito(str, enum.Enum):
    LIVRE = "livre"
    OCUPADO = "ocupado"
    MANUTENCAO = "manutencao"

class LeitoCreate(BaseModel):
    numero: str
    tipo: str
    localizacao: str

class LeitoResponse(LeitoCreate):
    id: int
    status: StatusLeito

    model_config = {
        "from_attributes": True
    }

class LeitoOut(BaseModel):
    id: int
    numero: str
    tipo: str
    status: str

    class Config:
        from_attributes = True