from pydantic import BaseModel, EmailStr
from enum import Enum

class TipoUsuario(str, Enum):
    ADMIN = "admin"
    MEDICO = "medico"
    ENFERMEIRO = "enfermeiro"
    PACIENTE = "paciente"

class UsuarioCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    tipo_usuario: TipoUsuario

class UsuarioResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    tipo_usuario: TipoUsuario

    model_config = {
        "from_attributes": True
    }
