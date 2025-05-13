```mermaid
erDiagram
    USUARIO {
        int id PK
        string username
        string hashed_password
        string tipo_usuario
        boolean ativo
    }

    PACIENTE {
        int id PK
        string nome
        int idade
        string sexo
        string endereco
        string email
        date data_nascimento
    }

    MEDICO {
        int id PK
        string nome
        string crm
        string especialidade
        string email
        string telefone
    }

    HOSPITAL {
        int id PK
        string nome
        string endereco
        string telefone
    }

    LEITO {
        int id PK
        string numero
        string tipo
        enum status
        string localizacao
        int hospital_id FK
    }

    INTERNACAO {
        int id PK
        int paciente_id FK
        int leito_id FK
        date data_entrada
        date data_alta
        string motivo
    }

    CONSULTA {
        int id PK
        int paciente_id FK
        int medico_id FK
        datetime data_hora
        string tipo
    }

    USUARIO ||--o{ MEDICO : "é"
    USUARIO ||--o{ PACIENTE : "é"
    HOSPITAL ||--o{ LEITO : "possui"
    PACIENTE ||--o{ CONSULTA : "agenda"
    MEDICO ||--o{ CONSULTA : "realiza"
    PACIENTE ||--o{ INTERNACAO : "possui"
    LEITO ||--o{ INTERNACAO : "recebe"
} 