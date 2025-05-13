from app.database import get_db, engine, Base
from app.models.paciente import Paciente
from app.models.medico import Medico
from app.models.consulta import Consulta
from app.models.hospital import Hospital
from app.models.leito import Leito, StatusLeito
from app.models.internacao import Internacao
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import random

def random_crm():
    return str(random.randint(10000, 99999))

def random_telefone():
    return f"(11) 9{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"

def random_email(nome, especialidade):
    nome_base = nome.lower().replace(" ", ".").replace(".", "")
    especialidade_base = especialidade.lower()
    return f"{nome_base}.{especialidade_base}@hospital.com"

def populate_database():
    print("Criando tabelas...")
    Base.metadata.create_all(bind=engine)
    
    db: Session = next(get_db())
    
    try:
        # Limpar todas as tabelas
        print("Limpando tabelas existentes...")
        db.query(Internacao).delete()
        db.query(Consulta).delete()
        db.query(Leito).delete()
        db.query(Paciente).delete()
        db.query(Medico).delete()
        db.query(Hospital).delete()
        db.commit()
        print("Tabelas limpas com sucesso!")
        
        # Criar hospitais
        hospitais = [
            Hospital(
                nome="Hospital São Lucas",
                endereco="Av. Paulista, 1000",
                telefone="(11) 3333-0001"
            ),
            Hospital(
                nome="Hospital Santa Clara",
                endereco="Rua Augusta, 500",
                telefone="(11) 3333-0002"
            ),
            Hospital(
                nome="Hospital São Francisco",
                endereco="Av. Brasil, 2000",
                telefone="(11) 3333-0003"
            )
        ]
        
        # Criar médicos
        medicos = [
            Medico(
                nome="Dr. Lucas Andrade",
                crm=random_crm(),
                especialidade="Cardiologia",
                email=random_email("Lucas Andrade", "Cardiologia"),
                telefone=random_telefone()
            ),
            Medico(
                nome="Dra. Fernanda Lima",
                crm=random_crm(),
                especialidade="Pediatria",
                email=random_email("Fernanda Lima", "Pediatria"),
                telefone=random_telefone()
            ),
            Medico(
                nome="Dr. Rafael Torres",
                crm=random_crm(),
                especialidade="Ortopedia",
                email=random_email("Rafael Torres", "Ortopedia"),
                telefone=random_telefone()
            ),
            Medico(
                nome="Dra. Camila Souza",
                crm=random_crm(),
                especialidade="Dermatologia",
                email=random_email("Camila Souza", "Dermatologia"),
                telefone=random_telefone()
            ),
            Medico(
                nome="Dr. Bruno Martins",
                crm=random_crm(),
                especialidade="Neurologia",
                email=random_email("Bruno Martins", "Neurologia"),
                telefone=random_telefone()
            )
        ]
        
        # Criar pacientes
        pacientes = [
            Paciente(
                nome="Patrícia Gomes",
                idade=29,
                sexo="F",
                endereco="Rua das Acácias, 101",
                email="patricia.gomes@email.com",
                data_nascimento=datetime(1994, 2, 14)
            ),
            Paciente(
                nome="Eduardo Ramos",
                idade=41,
                sexo="M",
                endereco="Av. Brasil, 202",
                email="eduardo.ramos@email.com",
                data_nascimento=datetime(1982, 6, 30)
            ),
            Paciente(
                nome="Juliana Pires",
                idade=36,
                sexo="F",
                endereco="Rua do Sol, 303",
                email="juliana.pires@email.com",
                data_nascimento=datetime(1987, 9, 5)
            ),
            Paciente(
                nome="Marcos Vinícius",
                idade=50,
                sexo="M",
                endereco="Av. Central, 404",
                email="marcos.vinicius@email.com",
                data_nascimento=datetime(1973, 12, 22)
            ),
            Paciente(
                nome="Sofia Carvalho",
                idade=24,
                sexo="F",
                endereco="Rua das Palmeiras, 505",
                email="sofia.carvalho@email.com",
                data_nascimento=datetime(1999, 4, 18)
            ),
            Paciente(
                nome="Henrique Dias",
                idade=60,
                sexo="M",
                endereco="Av. das Nações, 606",
                email="henrique.dias@email.com",
                data_nascimento=datetime(1963, 8, 11)
            )
        ]
        
        # Primeiro commit para obter os IDs
        db.add_all(hospitais)
        db.add_all(medicos)
        db.add_all(pacientes)
        db.commit()
        
        print("\nDados básicos inseridos com sucesso!")
        
        # Criar leitos
        leitos = []
        tipos_leito = ["UTI", "Enfermaria", "Semi-Intensivo"]
        
        for hospital in hospitais:
            for i in range(1, 11):  # 10 leitos por hospital
                leito = Leito(
                    numero=f"{hospital.id}0{i:02d}",
                    tipo=random.choice(tipos_leito),
                    status=random.choice(list(StatusLeito)),
                    localizacao=f"Ala {chr(65 + (i-1)//3)}"
                )
                leitos.append(leito)
        
        db.add_all(leitos)
        db.commit()
        
        # Buscar leitos livres já com id
        leitos_livres = db.query(Leito).filter(Leito.status == StatusLeito.LIVRE).all()
        
        # Criar consultas
        tipos_consulta = ["Primeira Consulta", "Retorno", "Avaliação", "Revisão", "Emergência"]
        consultas = []
        
        for paciente in pacientes:
            for _ in range(2):  # 2 consultas por paciente
                consulta = Consulta(
                    paciente_id=paciente.id,
                    profissional_id=random.choice([m.id for m in medicos]),
                    data_hora=datetime.now() + timedelta(days=random.randint(1, 30)),
                    tipo=random.choice(tipos_consulta)
                )
                consultas.append(consulta)
        
        # Criar internações
        internacoes = []
        for paciente in pacientes[:3]:  # Internações para os 3 primeiros pacientes
            if leitos_livres:
                leito_disponivel = leitos_livres.pop(0)
                data_entrada = datetime.now() - timedelta(days=random.randint(1, 10))
                data_alta = data_entrada + timedelta(days=random.randint(1, 5))
                
                internacao = Internacao(
                    paciente_id=paciente.id,
                    leito_id=leito_disponivel.id,
                    data_entrada=data_entrada,
                    data_alta=data_alta,
                    motivo=f"Tratamento de {random.choice(['Hipertensão', 'Diabetes', 'Pneumonia', 'Fraturas'])}"
                )
                internacoes.append(internacao)
                leito_disponivel.status = StatusLeito.OCUPADO
        
        # Segundo commit para os dados relacionados
        db.add_all(consultas)
        db.add_all(internacoes)
        db.commit()
        
        print("\nDados relacionados inseridos com sucesso!")
        
        print("\nHospitais criados:")
        for hospital in hospitais:
            print(f"- {hospital.nome}")
        
        print("\nMédicos criados:")
        for medico in medicos:
            print(f"- {medico.nome} ({medico.especialidade}) | CRM: {medico.crm}")
        
        print("\nPacientes criados:")
        for paciente in pacientes:
            print(f"- {paciente.nome}")
        
        print("\nLeitos criados:")
        for leito in leitos:
            print(f"- Leito {leito.numero} ({leito.tipo}) - {leito.status}")
        
        print("\nConsultas criadas:")
        for consulta in consultas:
            print(f"- {consulta.tipo} para paciente_id={consulta.paciente_id} com profissional_id={consulta.profissional_id}")
        
        print("\nInternações criadas:")
        for internacao in internacoes:
            print(f"- Paciente {internacao.paciente_id} internado no leito {internacao.leito_id}")
            
    except Exception as e:
        print(f"Erro ao inserir dados: {str(e)}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    populate_database() 