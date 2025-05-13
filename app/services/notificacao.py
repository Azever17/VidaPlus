# app/services/notificacao.py

def notificar_paciente(paciente_id: int, mensagem: str):
    print(f"[Notificação] Paciente {paciente_id}: {mensagem}")
