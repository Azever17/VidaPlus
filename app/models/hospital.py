from sqlalchemy import Column, Integer, String
from app.database import Base

class Hospital(Base):
    __tablename__ = "hospitais"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    telefone = Column(String)
