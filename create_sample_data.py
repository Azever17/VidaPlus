from app.database import get_db, Base, engine
from app.models.paciente import Paciente
from app.models.medico import Medico
from app.models.consulta import Consulta, StatusConsulta, TipoConsulta
from datetime import datetime, timedelta
from sqlalchemy.orm import Session

def create_sample_data():
    print("Iniciando criação de dados de exemplo...")
    
    # Garantir que as tabelas existem
    Base.metadata.create_all(bind=engine)
    print("Tabelas verificadas/criadas.")
    
    db: Session = next(get_db())
    print("Conexão com o banco estabelecida.")
    
    # Criar pacientes
    pacientes = [
        Paciente(
            nome="João Silva",
            idade=43,
            sexo="M",
            endereco="Rua A, 123",
            email="joao.silva@email.com",
            data_nascimento=datetime(1980, 1, 1)
        ),
        Paciente(
            nome="Maria Santos",
            idade=38,
            sexo="F",
            endereco="Rua B, 456",
            email="maria.santos@email.com",
            data_nascimento=datetime(1985, 5, 15)
        ),
        Paciente(
            nome="Pedro Oliveira",
            idade=33,
            sexo="M",
            endereco="Rua C, 789",
            email="pedro.oliveira@email.com",
            data_nascimento=datetime(1990, 10, 20)
        )
    ]
    
    # Criar médicos
    medicos = [
        Medico(
            nome="Dr. Carlos Souza",
            crm="12345-SP",
            especialidade="Cardiologia",
            email="carlos.souza@email.com",
            telefone="(11) 96666-6666"
        ),
        Medico(
            nome="Dra. Ana Lima",
            crm="54321-SP",
            especialidade="Pediatria",
            email="ana.lima@email.com",
            telefone="(11) 95555-5555"
        ),
        Medico(
            nome="Dr. Roberto Santos",
            crm="67890-SP",
            especialidade="Ortopedia",
            email="roberto.santos@email.com",
            telefone="(11) 94444-4444"
        )
    ]
    
    # Adicionar pacientes e médicos ao banco
    for paciente in pacientes:
        db.add(paciente)
    for medico in medicos:
        db.add(medico)
    
    db.commit()
    print("Pacientes e médicos criados com sucesso!")
    
    # Criar consultas
    hoje = datetime.now()
    consultas = [
        Consulta(
            paciente_id=1,
            profissional_id=1,
            data_hora=hoje + timedelta(days=1),
            tipo=TipoConsulta.PRESENCIAL
        ),
        Consulta(
            paciente_id=2,
            profissional_id=2,
            data_hora=hoje + timedelta(days=2),
            tipo=TipoConsulta.PRESENCIAL
        ),
        Consulta(
            paciente_id=3,
            profissional_id=3,
            data_hora=hoje + timedelta(days=3),
            tipo=TipoConsulta.PRESENCIAL
        )
    ]
    
    # Adicionar consultas ao banco
    for consulta in consultas:
        db.add(consulta)
    
    db.commit()
    print("Consultas criadas com sucesso!")
    print("Dados de exemplo criados com sucesso!")

if __name__ == "__main__":
    create_sample_data() 