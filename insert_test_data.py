import sqlite3
from datetime import datetime, timedelta

def conectar_banco():
    return sqlite3.connect('vida_plus.db')

def inserir_dados_teste():
    conn = conectar_banco()
    cursor = conn.cursor()
    
    try:
        # Inserir usuários
        usuarios = [
            ('admin', 'senha123', 'admin', True),
            ('medico1', 'senha123', 'medico', True),
            ('paciente1', 'senha123', 'paciente', True)
        ]
        cursor.executemany('INSERT INTO usuario (username, hashed_password, tipo_usuario, ativo) VALUES (?, ?, ?, ?)', usuarios)
        
        # Inserir pacientes
        pacientes = [
            ('João Silva', 45, 'M', 'Rua das Flores, 123', 'joao@email.com', '1978-05-15'),
            ('Maria Santos', 32, 'F', 'Av. Principal, 456', 'maria@email.com', '1991-08-22'),
            ('Pedro Oliveira', 28, 'M', 'Rua do Comércio, 789', 'pedro@email.com', '1995-03-10')
        ]
        cursor.executemany('INSERT INTO paciente (nome, idade, sexo, endereco, email, data_nascimento) VALUES (?, ?, ?, ?, ?, ?)', pacientes)
        
        # Inserir médicos
        medicos = [
            ('Dr. Carlos Mendes', '12345-SP', 'Cardiologia', 'carlos@hospital.com', '(11) 99999-1111'),
            ('Dra. Ana Costa', '67890-SP', 'Pediatria', 'ana@hospital.com', '(11) 99999-2222'),
            ('Dr. Roberto Lima', '54321-SP', 'Ortopedia', 'roberto@hospital.com', '(11) 99999-3333')
        ]
        cursor.executemany('INSERT INTO medico (nome, crm, especialidade, email, telefone) VALUES (?, ?, ?, ?, ?)', medicos)
        
        # Inserir hospitais
        hospitais = [
            ('Hospital São Lucas', 'Av. Paulista, 1000', '(11) 3333-4444'),
            ('Clínica Santa Maria', 'Rua Augusta, 500', '(11) 3333-5555')
        ]
        cursor.executemany('INSERT INTO hospital (nome, endereco, telefone) VALUES (?, ?, ?)', hospitais)
        
        # Inserir leitos
        leitos = [
            ('101', 'Enfermaria', 'Disponível', '1º Andar', 1),
            ('102', 'UTI', 'Ocupado', '2º Andar', 1),
            ('201', 'Quarto Particular', 'Disponível', '3º Andar', 2)
        ]
        cursor.executemany('INSERT INTO leito (numero, tipo, status, localizacao, hospital_id) VALUES (?, ?, ?, ?, ?)', leitos)
        
        # Inserir internações
        data_atual = datetime.now()
        internacoes = [
            (1, 2, data_atual - timedelta(days=2), None, 'Dor no peito'),
            (2, 3, data_atual - timedelta(days=1), None, 'Fratura no braço')
        ]
        cursor.executemany('INSERT INTO internacao (paciente_id, leito_id, data_entrada, data_alta, motivo) VALUES (?, ?, ?, ?, ?)', internacoes)
        
        # Inserir consultas
        consultas = [
            (1, 1, data_atual + timedelta(days=1), 'Retorno'),
            (2, 2, data_atual + timedelta(days=2), 'Primeira Consulta'),
            (3, 3, data_atual + timedelta(days=3), 'Avaliação')
        ]
        cursor.executemany('INSERT INTO consulta (paciente_id, profissional_id, data_hora, tipo) VALUES (?, ?, ?, ?)', consultas)
        
        conn.commit()
        print("Dados de teste inseridos com sucesso!")
        
    except sqlite3.Error as e:
        print(f"Erro ao inserir dados: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == '__main__':
    inserir_dados_teste() 