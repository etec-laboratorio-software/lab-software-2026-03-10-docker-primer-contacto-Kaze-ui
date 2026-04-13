# backend/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

# --- Configuración de SQLite ---
# Lee de la variable de entorno DATABASE_URL si existe (Docker),
# si no, usa la ruta local por defecto (desarrollo sin Docker)
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./sql_app.db")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    # 'connect_args' es necesario solo para SQLite
    # para permitir que sea usado por múltiples hilos (como FastAPI)
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()