from pydantic import BaseModel
from typing import Optional


class ProfissionalBase(BaseModel):
    nome: str
    especialidade: Optional[str] = None
    telefone: Optional[str] = None


class ProfissionalCreate(ProfissionalBase):
    pass


class ProfissionalUpdate(ProfissionalBase):
    pass


class ProfissionalOut(ProfissionalBase):
    id: int

    class Config:
        from_attributes = True
