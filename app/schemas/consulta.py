from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TipoConsulta(str, Enum):
    PRESENCIAL = "presencial"
    ONLINE = "online"


class ConsultaRequest(BaseModel):
    paciente_id: int
    medico_id: int
    data_hora: datetime
    tipo: str  # presencial ou online

class ConsultaResponse(BaseModel):
    id: int
    paciente_id: int
    medico_id: int
    data_hora: datetime
    tipo: str
    status: str
    link_videoconferencia: Optional[str] = None

    class Config:
        from_attributes = True
