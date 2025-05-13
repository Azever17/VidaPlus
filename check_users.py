from app.database import get_db
from app.models.usuario import UsuarioORM
from sqlalchemy.orm import Session
from app.auth.jwt import hash_password

def list_users():
    print("Listando usuários cadastrados...")
    
    db: Session = next(get_db())
    
    users = db.query(UsuarioORM).all()
    
    if not users:
        print("Nenhum usuário encontrado no banco de dados.")
        return
    
    print("\nUsuários cadastrados:")
    print("-" * 50)
    for user in users:
        print(f"ID: {user.id}")
        print(f"Username: {user.username}")
        print(f"Tipo: {user.tipo_usuario}")
        print(f"Ativo: {user.ativo}")
        print(f"Hash da senha: {user.hashed_password}")
        print("-" * 50)
    
    # Gerar novo hash para comparação
    print("\nGerando novo hash para a senha 'senha1234':")
    new_hash = hash_password("senha1234")
    print(f"Novo hash: {new_hash}")

if __name__ == "__main__":
    list_users() 