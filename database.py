from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Endereço do banco de dados
SQLALCHEMY_DATABASE_URL = "sqlite:///./taskflow.db"

# Criando o motor do banco
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependência para abrir/fechar a conexão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()