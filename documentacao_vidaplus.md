# VidaPlus - Sistema de Gestão de Consultas Médicas

## Sumário
1. [Introdução](#introdução)
2. [Requisitos](#requisitos)
3. [Modelagem](#modelagem)
4. [Implementação](#implementação)
5. [Plano de Testes](#plano-de-testes)
6. [Conclusão](#conclusão)
7. [Referências](#referências)

## Introdução

O VidaPlus é um sistema de gestão de consultas médicas desenvolvido para facilitar o agendamento e gerenciamento de consultas entre pacientes e profissionais de saúde. O sistema visa modernizar e otimizar o processo de agendamento de consultas, oferecendo uma interface intuitiva e funcionalidades essenciais para a gestão de uma clínica médica.

### Objetivos
- Automatizar o processo de agendamento de consultas
- Gerenciar cadastro de pacientes e profissionais
- Facilitar o acesso às informações médicas
- Melhorar a comunicação entre pacientes e profissionais
- Otimizar o tempo de gestão da clínica

## Requisitos

### Requisitos Funcionais (RF)

#### Implementados ✅
1. RF01 - Cadastro de pacientes
   - Cadastrar novos pacientes
   - Atualizar dados de pacientes
   - Excluir pacientes
   - Listar pacientes

2. RF02 - Cadastro de profissionais
   - Cadastrar novos profissionais
   - Atualizar dados profissionais
   - Excluir profissionais
   - Listar profissionais

3. RF03 - Gestão de consultas
   - Agendar consultas
   - Cancelar consultas
   - Listar consultas
   - Visualizar histórico

4. RF04 - Autenticação e autorização
   - Login de usuários
   - Controle de acesso
   - Gerenciamento de sessões


### Requisitos Não Funcionais (RNF)

#### Implementados ✅
1. RNF01 - Segurança
   - Autenticação JWT
   - Criptografia de senhas
   - Controle de acesso

2. RNF02 - Performance
   - Resposta rápida das APIs
   - Otimização de consultas

3. RNF03 - Usabilidade
   - Interface intuitiva
   - Documentação clara


## Modelagem

### Diagrama de Classes
```
[Paciente]
- id: int
- nome: string
- idade: int
- sexo: string
- endereco: string
- email: string
- data_nascimento: date

[Profissional]
- id: int
- nome: string
- crm: string
- especialidade: string
- email: string
- telefone: string

[Consulta]
- id: int
- paciente_id: int
- profissional_id: int
- data_hora: datetime
- tipo: string
- status: string
```

### Casos de Uso

1. **Gestão de Pacientes**
   - Ator: Administrador
   - Ações:
     - Cadastrar paciente
     - Atualizar dados
     - Excluir paciente
     - Listar pacientes

2. **Gestão de Profissionais**
   - Ator: Administrador
   - Ações:
     - Cadastrar profissional
     - Atualizar dados
     - Excluir profissional
     - Listar profissionais

3. **Gestão de Consultas**
   - Ator: Administrador
   - Ações:
     - Agendar consulta
     - Cancelar consulta
     - Listar consultas
     - Visualizar histórico

## Implementação

### Tecnologias Utilizadas
- Backend: Python com FastAPI
- Banco de Dados: SQLite
- Autenticação: JWT
- Documentação: Swagger/OpenAPI

### Estrutura do Projeto
```
vidaplus/
├── app/
│   ├── models/
│   ├── schemas/
│   ├── routes/
│   └── database.py
├── tests/
├── alembic/
└── requirements.txt
```

### Link do GitHub
[Link do Repositório](https://github.com/seu-usuario/vidaplus)

## Plano de Testes

### Testes de API

1. **Autenticação**
   - Entrada: 
     ```json
     {
         "username": "admin",
         "password": "senha1234"
     }
     ```
   - Saída: Token JWT
   - Resultado: ✅ Sucesso
   - Endpoint: POST /auth/token

2. **Gestão de Pacientes**
   - **Cadastro de Paciente**
     - Entrada:
     ```json
     {
         "nome": "Novo Paciente",
         "idade": 30,
         "sexo": "M",
         "endereco": "Rua Nova, 123",
         "email": "novo.paciente@email.com",
         "data_nascimento": "1994-01-01"
     }
     ```
     - Endpoint: POST /pacientes
     - Resultado: ✅ Sucesso

   - **Atualização de Paciente**
     - Entrada:
     ```json
     {
         "nome": "Paciente Atualizado",
         "idade": 31,
         "endereco": "Rua Atualizada, 456"
     }
     ```
     - Endpoint: PUT /pacientes/{id}
     - Resultado: ✅ Sucesso

   - **Listagem de Pacientes**
     - Endpoint: GET /pacientes
     - Resultado: ✅ Lista de pacientes retornada

   - **Exclusão de Paciente**
     - Endpoint: DELETE /pacientes/{id}
     - Resultado: ✅ Sucesso

3. **Gestão de Profissionais**
   - **Cadastro de Profissional**
     - Entrada:
     ```json
     {
         "nome": "Dr. Novo Médico",
         "crm": "98765-SP",
         "especialidade": "Neurologia",
         "email": "novo.medico@email.com",
         "telefone": "(11) 93333-3333"
     }
     ```
     - Endpoint: POST /profissionais
     - Resultado: ✅ Sucesso

   - **Atualização de Profissional**
     - Entrada:
     ```json
     {
         "nome": "Dr. Médico Atualizado",
         "especialidade": "Cardiologia",
         "telefone": "(11) 94444-4444"
     }
     ```
     - Endpoint: PUT /profissionais/{id}
     - Resultado: ✅ Sucesso

   - **Listagem de Profissionais**
     - Endpoint: GET /profissionais
     - Resultado: ✅ Lista de profissionais retornada

   - **Exclusão de Profissional**
     - Endpoint: DELETE /profissionais/{id}
     - Resultado: ✅ Sucesso

4. **Gestão de Consultas**
   - **Agendamento de Consulta**
     - Entrada:
     ```json
     {
         "paciente_id": 1,
         "profissional_id": 1,
         "data_hora": "2024-03-25T10:00:00",
         "tipo": "presencial"
     }
     ```
     - Endpoint: POST /consultas
     - Resultado: ✅ Sucesso

   - **Listagem de Consultas**
     - Endpoint: GET /consultas/proximas
     - Resultado: ✅ Lista de consultas retornada

   - **Cancelamento de Consulta**
     - Endpoint: PUT /consultas/{id}/cancelar
     - Resultado: ✅ Sucesso

### Testes de Integração
- Verificação de relacionamentos entre entidades
  - Paciente -> Consulta
  - Profissional -> Consulta
- Validação de regras de negócio
  - Horários disponíveis
  - Conflitos de agenda
  - Permissões de acesso
- Testes de fluxo completo
  - Cadastro -> Agendamento -> Cancelamento
  - Atualização de dados -> Verificação de consultas

### Testes de Segurança
- Validação de token JWT
- Controle de acesso por perfil
- Proteção contra acesso não autorizado
- Validação de dados de entrada

### Testes de Performance
- Tempo de resposta das APIs
- Carga de múltiplas requisições
- Otimização de consultas ao banco

## Conclusão

### O que foi feito
- Sistema completo de gestão de consultas
- API RESTful com FastAPI
- Autenticação e autorização
- CRUD completo para pacientes e profissionais
- Gestão de consultas

### Aprendizados
- Desenvolvimento com FastAPI
- Implementação de JWT
- Modelagem de banco de dados
- Testes de API
- Documentação de software

### Dificuldades
- Implementação de autenticação
- Relacionamentos no banco de dados
- Testes de integração
- Documentação da API

## Referências

### Frameworks e Bibliotecas
- FastAPI: https://fastapi.tiangolo.com/
- SQLAlchemy: https://www.sqlalchemy.org/
- Pydantic: https://pydantic-docs.helpmanual.io/
- JWT: https://jwt.io/

### Tutoriais e Documentação
- FastAPI Tutorial: https://fastapi.tiangolo.com/tutorial/
- SQLAlchemy Documentation: https://docs.sqlalchemy.org/
- JWT Authentication: https://fastapi.tiangolo.com/tutorial/security/

### Ferramentas
- Postman: https://www.postman.com/
- SQLite: https://www.sqlite.org/
- Git: https://git-scm.com/ 