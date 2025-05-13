from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from app.database import Base, engine
from app.routes_folder import (
    user_routes,
    paciente_routes,
    profissional_routes,
    notificacao_routes,
    auth_routes,
    consulta_routes,
    dashboard_routes,
    leito_routes,
    hospital_routes,
    internacao_routes
)


# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

# Inicialização da aplicação
app = FastAPI(
    title="SGHSS - Sistema de Gestão Hospitalar",
    description="Sistema de Gestão Hospitalar desenvolvido por Marcelo Azevedo (RU: 4312882)",
    version="1.0.0"
)

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuração de arquivos estáticos e templates
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Registro das rotas
app.include_router(user_routes.router, prefix="/auth", tags=["Autenticação"])  # cadastro de usuários
app.include_router(auth_routes.router, prefix="/auth", tags=["Autenticação"])  # login/token
app.include_router(paciente_routes.router, prefix="/pacientes", tags=["Pacientes"])
app.include_router(profissional_routes.router, prefix="/profissionais", tags=["Profissionais"])
app.include_router(notificacao_routes.router, prefix="/notificacoes", tags=["Notificações"])
app.include_router(consulta_routes.router, prefix="/consultas", tags=["Consultas"])
app.include_router(dashboard_routes.router, prefix="/dashboard", tags=["Dashboard"])
app.include_router(leito_routes.router, prefix="/leitos", tags=["Leitos"])
app.include_router(hospital_routes.router, prefix="/hospitais", tags=["Hospitais"])
app.include_router(internacao_routes.router, prefix="/internacoes", tags=["Internações"])

@app.get("/")
async def root():
    return RedirectResponse(url="/login")

@app.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/dashboard")
async def dashboard_page(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})
