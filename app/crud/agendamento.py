# app/crud/agendamento_crud.py

from sqlalchemy.orm import Session
from app.models.agendamento import Agendamento
from app.models.paciente import Paciente
from app.models.profissional import Profissional
from app.schemas.agendamento import AgendamentoCreate
from app.utils import generate_report  # Função de geração de laudo
import os


def finalizar_consulta(db: Session, agendamento_id: int):
    agendamento = db.query(Agendamento).filter(Agendamento.id == agendamento_id).first()

    if not agendamento:
        raise Exception("Agendamento não encontrado")

    if agendamento.status == 'realizado':
        raise Exception("Consulta já finalizada")

    # Gerar o laudo
    content = f"Laudo da consulta de {agendamento.paciente.nome} com {agendamento.profissional.nome}"
    laudo_pdf = generate_report(content)  # Função para gerar o laudo em PDF

    # Salvar o laudo em algum lugar ou banco de dados
    laudo_path = os.path.join("laudos", f"laudo_{agendamento_id}.pdf")
    with open(laudo_path, 'wb') as f:
        f.write(laudo_pdf.getvalue())

    agendamento.laudo_url = laudo_path
    agendamento.status = "realizado"

    db.commit()
    db.refresh(agendamento)

    return agendamento
