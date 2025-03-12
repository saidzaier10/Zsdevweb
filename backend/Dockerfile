FROM python:3.9-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHUNBUFFERED 1

# Dépendances système (adapté pour macOS/Docker)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Script d'entrée (pas besoin de dos2unix sur macOS)
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# Dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /app/frontend/dist/static

# Copie du code
COPY . .

ENTRYPOINT ["/app/entrypoint.sh"]