from enum import Enum


class TipoUsuario(str, Enum):  # OBS: Herdar de str é essencial!
    ADMIN = "admin"
    MEDICO = "medico"
    ENFERMEIRO = "enfermeiro"
    PACIENTE = "paciente"
