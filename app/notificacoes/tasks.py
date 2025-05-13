from app import celery
from app.notificacoes import enviar_email, enviar_sms


@celery.task
def tarefa_enviar_email(email, consulta_data):
    mensagem = f"Você tem uma consulta marcada para {consulta_data}."
    enviar_email(email, "Lembrete de Consulta", mensagem)

@celery.task
def tarefa_enviar_sms(telefone, consulta_data):
    mensagem = f"Lembrete: consulta em {consulta_data}."
    enviar_sms(telefone, mensagem)

