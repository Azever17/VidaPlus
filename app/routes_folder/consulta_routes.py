from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.models.consulta import Consulta
from app.schemas.consulta import ConsultaRequest, ConsultaResponse
from app.database import get_db
from app.dependencies import get_current_user


router = APIRouter()

@router.post("/", response_model=ConsultaResponse)
def agendar_consulta(consulta: ConsultaRequest, current_user: dict = Depends(get_current_user)):
    # Simulação de ID automático
    novo_id = len(consultas_fake_db) + 1
    nova_consulta = Consulta(**consulta.dict(), id=novo_id)

    # Verifica se o médico já tem consulta no mesmo horário
    for c in consultas_fake_db:
        if c.medico_id == nova_consulta.medico_id and c.data_hora == nova_consulta.data_hora:
            raise HTTPException(status_code=400, detail="Médico já possui consulta nesse horário.")

    consultas_fake_db.append(nova_consulta)

    # Envia a notificação
    try:
        notificar_paciente(nova_consulta.paciente_id, "Sua consulta foi agendada com sucesso.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Falha ao enviar notificação: {str(e)}")

    return nova_consulta

@router.put("/{consulta_id}/cancelar", response_model=ConsultaResponse)
def cancelar_consulta(consulta_id: int, current_user: dict = Depends(get_current_user)):
    for consulta in consultas_fake_db:
        if consulta.id == consulta_id:
            if consulta.status == "Cancelada":
                raise HTTPException(status_code=400, detail="Consulta já está cancelada.")
            consulta.status = "Cancelada"

            try:
                notificar_paciente(consulta.paciente_id, "Sua consulta foi cancelada.")
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Falha ao enviar notificação: {str(e)}")

            return consulta
    raise HTTPException(status_code=404, detail="Consulta não encontrada.")
