from app.models.usuario import Usuario, TipoUsuario

usuarios_fake_db = [
    Usuario(id=1, nome="Admin", email="admin@hospital.com", senha="admin", tipo=TipoUsuario.admin),
    Usuario(id=2, nome="Dr. João", email="joao@hospital.com", senha="medico123", tipo=TipoUsuario.medico),
    Usuario(id=3, nome="Maria", email="maria@paciente.com", senha="paciente123", tipo=TipoUsuario.paciente),
]
