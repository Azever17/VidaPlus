# app/routes/laudo_routes.py

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os

router = APIRouter()

LAUDO_DIR = "laudos"  # Certifique-se de que este diretório está correto


@router.get("/laudos/{laudo_filename}", response_class=FileResponse)
def download_laudo(laudo_filename: str):
    laudo_path = os.path.join(LAUDO_DIR, laudo_filename)

    if not os.path.exists(laudo_path):
        raise HTTPException(status_code=404, detail="Laudo não encontrado.")

    return FileResponse(path=laudo_path, media_type='application/pdf', filename=laudo_filename)

consulta.laudo_path = f"laudos/laudo_{consulta.id}.pdf"
db.commit()