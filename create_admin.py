# create_admin.py
from app.database import get_db, Base, engine
from app.models.usuario import UsuarioORM
from app.auth.jwt import hash_password
from sqlalchemy.orm import Session

def create_admin_user():
    print("Iniciando criação/atualização do usuário admin...")
    
    # Garantir que as tabelas existem
    Base.metadata.create_all(bind=engine)
    print("Tabelas verificadas/criadas.")
    
    db: Session = next(get_db())
    print("Conexão com o banco estabelecida.")
    
    existing_user = db.query(UsuarioORM).filter(UsuarioORM.username == "admin").first()
    print(f"Usuário admin existente: {existing_user is not None}")

    if existing_user:
        print("Atualizando senha do usuário admin...")
        existing_user.hashed_password = hash_password("senha1234")
        db.commit()
        print("Senha do usuário admin atualizada com sucesso!")
    else:
        print("Criando novo usuário admin...")
        admin_user = UsuarioORM(
            username="admin",
            hashed_password=hash_password("senha1234"),
            tipo_usuario="admin",
            ativo=True
        )
        db.add(admin_user)
        db.commit()
        print("Usuário admin criado com sucesso!")

if __name__ == "__main__":
    create_admin_user()
