from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes import auth_routes, paciente_routes, consulta_routes, dashboard_routes
from app.database import engine, Base

# Criar tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="VidaPlus")

# Montar rotas
app.include_router(auth_routes.router, prefix="/auth", tags=["Autenticação"])
app.include_router(paciente_routes.router, prefix="/api/pacientes", tags=["Pacientes"])
app.include_router(consulta_routes.router, prefix="/api/consultas", tags=["Consultas"])
app.include_router(dashboard_routes.router, prefix="/api/dashboard", tags=["Dashboard"])

# Configurar arquivos estáticos e templates
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
