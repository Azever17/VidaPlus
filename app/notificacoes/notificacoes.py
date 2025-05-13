import os
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from twilio.rest import Client
from datetime import datetime, timedelta
from tasks import tarefa_enviar_email, tarefa_enviar_sms


def agendar_notificacoes(email, telefone, data_consulta):
    data_consulta_dt = datetime.strptime(data_consulta, '%Y-%m-%d %H:%M')

    tarefa_enviar_email.apply_async((email, data_consulta), eta=data_consulta_dt - timedelta(days=1))
    tarefa_enviar_sms.apply_async((telefone, data_consulta), eta=data_consulta_dt - timedelta(hours=3))


def enviar_sms(destinatario, mensagem):
    client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
    message = client.messages.create(
        body=mensagem,
        from_=os.getenv("TWILIO_PHONE_NUMBER"),
        to=destinatario
    )
    return message.sid

def enviar_email(destinatario, assunto, mensagem):
    sg = sendgrid.SendGridAPIClient(api_key=os.getenv("SENDGRID_API_KEY"))
    from_email = Email("no-reply@hospital.com")
    to_email = To(destinatario)
    content = Content("text/plain", mensagem)
    mail = Mail(from_email, to_email, assunto, content)
    return sg.send(mail)

