from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()


# Modelo de notificação
class Notificacao(BaseModel):
    id: Optional[int] = None  # Agora o id é opcional
    paciente_id: int
    mensagem: str


# Banco simulado
notificacoes_fake_db: List[Notificacao] = []

# Variável para controle do ID (apenas para simulação)
ultimo_id = 0


# Enviar notificação
@router.post("/", response_model=Notificacao)
def enviar_notificacao(notificacao: Notificacao):
    global ultimo_id

    # Geração automática do ID (simulação)
    ultimo_id += 1
    notificacao.id = ultimo_id

    # Validação simples: A mensagem não pode estar vazia
    if not notificacao.mensagem:
        raise HTTPException(status_code=400, detail="A mensagem da notificação não pode estar vazia.")

    notificacoes_fake_db.append(notificacao)
    return notificacao


# Listar notificações
@router.get("/", response_model=List[Notificacao])
def listar_notificacoes():
    if not notificacoes_fake_db:
        raise HTTPException(status_code=404, detail="Nenhuma notificação encontrada.")
    return notificacoes_fake_db
