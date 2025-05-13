# app/db/fake_user.py
from typing import List

from app.models.usuario import Usuario, TipoUsuario

# Banco de dados simulado com TipoUsuario
usuarios_fake_db: List[Usuario] = [
    Usuario(id=1, nome="João", email="joao@exemplo.com", senha="1234", tipo_usuario=TipoUsuario.MEDICO),
    Usuario(id=2, nome="Maria", email="maria@exemplo.com", senha="1234",tipo_usuario=TipoUsuario.PACIENTE),
    # Adicione mais usuários conforme necessário
]
