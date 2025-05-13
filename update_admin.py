from app.database import get_db
from app.models.usuario import UsuarioORM
from app.auth.jwt import hash_password
from sqlalchemy.orm import Session

def update_admin_password():
    print("Atualizando senha do admin...")
    
    db: Session = next(get_db())
    
    admin = db.query(UsuarioORM).filter(UsuarioORM.username == "admin").first()
    
    if not admin:
        print("Usuário admin não encontrado!")
        return
    
    # Atualizar senha
    admin.hashed_password = hash_password("master")
    db.commit()
    
    print("Senha do admin atualizada com sucesso!")
    print(f"Novo hash: {admin.hashed_password}")

if __name__ == "__main__":
    update_admin_password() 