from pydantic import BaseModel

class PacienteBase(BaseModel):
    nome: str
    idade: int
    sexo: str
    endereco: str

class PacienteCreate(PacienteBase):
    pass

class PacienteUpdate(BaseModel):
    nome: str | None = None
    idade: int | None = None
    sexo: str | None = None
    endereco: str | None = None

class PacienteOut(PacienteBase):
    id: int

    class Config:
        from_attributes = True
