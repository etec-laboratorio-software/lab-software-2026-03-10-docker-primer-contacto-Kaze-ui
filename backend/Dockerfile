FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar e instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código del backend
COPY . .

# Crear directorio para la base de datos y dar permisos
RUN mkdir -p /app/data

# Script de inicio: corre migraciones y luego levanta el servidor
CMD alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8000