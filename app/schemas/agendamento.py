from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AgendamentoBase(BaseModel):
    paciente_id: int
    profissional_id: int
    data_hora: datetime

class AgendamentoCreate(AgendamentoBase):
    pass

class Agendamento(AgendamentoBase):
    id: int
    status: Optional[str] = "agendado"

    class Config:
        from_attributes = True
