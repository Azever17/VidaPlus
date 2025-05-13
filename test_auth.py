from app.database import get_db
from app.models.usuario import UsuarioORM
from app.auth.jwt import verify_password, hash_password
from sqlalchemy.orm import Session

def test_auth():
    print("Testando autenticação...")
    
    db: Session = next(get_db())
    
    # Buscar usuário admin
    admin = db.query(UsuarioORM).filter(UsuarioORM.username == "admin").first()
    
    if not admin:
        print("Usuário admin não encontrado!")
        return
    
    print(f"\nDados do usuário admin:")
    print(f"Username: {admin.username}")
    print(f"Hash da senha: {admin.hashed_password}")
    
    # Testar senha
    senha = "master"
    print(f"\nTestando senha: {senha}")
    
    # Gerar novo hash para comparação
    novo_hash = hash_password(senha)
    print(f"Novo hash gerado: {novo_hash}")
    
    # Verificar senha
    resultado = verify_password(senha, admin.hashed_password)
    print(f"\nResultado da verificação: {resultado}")
    
    if resultado:
        print("Senha correta!")
    else:
        print("Senha incorreta!")

if __name__ == "__main__":
    test_auth() 