```mermaid
classDiagram
    class Usuario {
        +Integer id
        +String username
        +String hashed_password
        +String tipo_usuario
        +Boolean ativo
    }

    class Paciente {
        +Integer id
        +String nome
        +Integer idade
        +String sexo
        +String endereco
        +String email
        +Date data_nascimento
    }

    class Medico {
        +Integer id
        +String nome
        +String crm
        +String especialidade
        +String email
        +String telefone
    }

    class Hospital {
        +Integer id
        +String nome
        +String endereco
        +String telefone
    }

    class Leito {
        +Integer id
        +String numero
        +String tipo
        +StatusLeito status
        +String localizacao
    }

    class Internacao {
        +Integer id
        +Integer paciente_id
        +Integer leito_id
        +Date data_entrada
        +Date data_alta
        +String motivo
    }

    class Consulta {
        +Integer id
        +Integer paciente_id
        +Integer profissional_id
        +DateTime data_hora
        +String tipo
    }

    Usuario <|-- Medico
    Usuario <|-- Paciente
    Hospital "1" -- "n" Leito
    Paciente "1" -- "n" Consulta
    Medico "1" -- "n" Consulta
    Paciente "1" -- "n" Internacao
    Leito "1" -- "n" Internacao
} 