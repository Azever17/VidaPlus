from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class PacienteInfo(BaseModel):
    id: int
    nome: str

class MedicoInfo(BaseModel):
    id: int
    nome: str
    especialidade: str

class DashboardStats(BaseModel):
    total_pacientes: int
    total_medicos: int
    consultas_hoje: int
    consultas_semana: int
    pacientes_lista: List[PacienteInfo]
    medicos_lista: List[MedicoInfo]

class PacienteResponse(BaseModel):
    id: int
    nome: str
    cpf: str
    data_nascimento: datetime
    sexo: str
    telefone: str
    email: str
    endereco: str

    class Config:
        from_attributes = True

class MedicoResponse(BaseModel):
    id: int
    nome: str
    crm: str
    especialidade: str
    email: str
    telefone: str

    class Config:
        from_attributes = True

class ConsultaResponse(BaseModel):
    id: int
    paciente_id: int
    medico_id: int
    data_hora: datetime
    tipo: str
    status: str
    observacoes: Optional[str] = None
    paciente: PacienteResponse
    medico: MedicoResponse

    class Config:
        from_attributes = True 