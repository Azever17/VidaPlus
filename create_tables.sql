-- Criação da tabela USUARIO
CREATE TABLE usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    hashed_password VARCHAR(255) NOT NULL,
    tipo_usuario VARCHAR(20) NOT NULL,
    ativo BOOLEAN DEFAULT TRUE
);

-- Criação da tabela PACIENTE
CREATE TABLE paciente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    idade INTEGER NOT NULL,
    sexo CHAR(1) NOT NULL,
    endereco VARCHAR(200) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    data_nascimento DATE NOT NULL
);

-- Criação da tabela MEDICO
CREATE TABLE medico (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    crm VARCHAR(20) NOT NULL UNIQUE,
    especialidade VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefone VARCHAR(20) NOT NULL
);

-- Criação da tabela HOSPITAL
CREATE TABLE hospital (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(200) NOT NULL,
    telefone VARCHAR(20) NOT NULL
);

-- Criação da tabela LEITO
CREATE TABLE leito (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero VARCHAR(10) NOT NULL UNIQUE,
    tipo VARCHAR(50) NOT NULL,
    status VARCHAR(20) NOT NULL,
    localizacao VARCHAR(100) NOT NULL,
    hospital_id INTEGER NOT NULL,
    FOREIGN KEY (hospital_id) REFERENCES hospital(id)
);

-- Criação da tabela INTERNACAO
CREATE TABLE internacao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paciente_id INTEGER NOT NULL,
    leito_id INTEGER NOT NULL,
    data_entrada DATETIME NOT NULL,
    data_alta DATETIME,
    motivo TEXT NOT NULL,
    FOREIGN KEY (paciente_id) REFERENCES paciente(id),
    FOREIGN KEY (leito_id) REFERENCES leito(id)
);

-- Criação da tabela CONSULTA
CREATE TABLE consulta (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paciente_id INTEGER NOT NULL,
    profissional_id INTEGER NOT NULL,
    data_hora DATETIME NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    FOREIGN KEY (paciente_id) REFERENCES paciente(id),
    FOREIGN KEY (profissional_id) REFERENCES medico(id)
);

-- Índices para melhorar performance
CREATE INDEX idx_paciente_email ON paciente(email);
CREATE INDEX idx_medico_crm ON medico(crm);
CREATE INDEX idx_medico_email ON medico(email);
CREATE INDEX idx_leito_numero ON leito(numero);
CREATE INDEX idx_leito_hospital ON leito(hospital_id);
CREATE INDEX idx_internacao_paciente ON internacao(paciente_id);
CREATE INDEX idx_internacao_leito ON internacao(leito_id);
CREATE INDEX idx_consulta_paciente ON consulta(paciente_id);
CREATE INDEX idx_consulta_profissional ON consulta(profissional_id);
CREATE INDEX idx_consulta_data ON consulta(data_hora); 