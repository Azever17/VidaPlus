from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.paciente import Paciente
from app.models.consulta import Consulta
from app.models.medico import Medico
from datetime import datetime, timedelta
from typing import List
from app.schemas.dashboard import DashboardStats, ConsultaResponse, MedicoResponse

router = APIRouter()

@router.get("/stats", response_model=DashboardStats)
def get_dashboard_stats(db: Session = Depends(get_db)):
    """Retorna estatísticas para o dashboard"""
    try:
        # Total de pacientes e lista
        pacientes = db.query(Paciente).all()
        total_pacientes = len(pacientes)
        pacientes_lista = [{"id": p.id, "nome": p.nome} for p in pacientes]

        # Total de médicos e lista
        medicos = db.query(Medico).all()
        total_medicos = len(medicos)
        medicos_lista = [{"id": m.id, "nome": m.nome, "especialidade": m.especialidade} for m in medicos]
        
        # Consultas de hoje
        hoje = datetime.now().date()
        consultas_hoje = db.query(Consulta).filter(
            Consulta.data_hora >= hoje,
            Consulta.data_hora < hoje + timedelta(days=1)
        ).count()
        
        # Consultas da semana
        inicio_semana = hoje - timedelta(days=hoje.weekday())
        fim_semana = inicio_semana + timedelta(days=7)
        consultas_semana = db.query(Consulta).filter(
            Consulta.data_hora >= inicio_semana,
            Consulta.data_hora < fim_semana
        ).count()
        
        return DashboardStats(
            total_pacientes=total_pacientes,
            total_medicos=total_medicos,
            consultas_hoje=consultas_hoje,
            consultas_semana=consultas_semana,
            pacientes_lista=pacientes_lista,
            medicos_lista=medicos_lista
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/consultas/proximas", response_model=List[ConsultaResponse])
def get_proximas_consultas(db: Session = Depends(get_db)):
    """Retorna as próximas consultas"""
    try:
        consultas = db.query(Consulta).filter(
            Consulta.data_hora >= datetime.now()
        ).order_by(Consulta.data_hora).limit(5).all()
        
        return consultas
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

