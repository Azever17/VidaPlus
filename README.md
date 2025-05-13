# SGHSS - Sistema de Gestão Hospitalar

Sistema de Gestão Hospitalar desenvolvido por Marcelo Azevedo (RU: 4312882)

## Requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)

## Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd VidaPlus_Marcelo
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
```
DATABASE_URL=sqlite:///./vida_plus.db
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Executando o Projeto

1. Inicie o servidor:
```bash
uvicorn app.main:app --reload
```

2. Acesse a documentação da API:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Executando os Testes

```bash
pytest
```

## Estrutura do Projeto

```
app/
├── auth/           # Autenticação e autorização
├── crud/          # Operações CRUD
├── models/        # Modelos do banco de dados
├── routes/        # Rotas da API
├── schemas/       # Schemas Pydantic
├── services/      # Serviços de negócio
└── utils/         # Utilitários
```

## Funcionalidades

- Autenticação de usuários
- Gestão de pacientes
- Gestão de profissionais
- Gestão de consultas
- Gestão de leitos
- Gestão de internações
- Dashboard
- Sistema de notificações
