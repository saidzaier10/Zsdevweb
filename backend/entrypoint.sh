#!/bin/sh

# Attente PostgreSQL avec timeout amélioré
echo "⌛ Attente de PostgreSQL..."
timeout=30
while ! nc -z db 5432; do
  sleep 1
  timeout=$((timeout-1))
  [ $timeout -le 0 ] && echo "❌ PostgreSQL non disponible" && exit 1
done
echo "✅ PostgreSQL prêt !"

# Migrations
python manage.py makemigrations
python manage.py migrate

# Superutilisateur (optionnel)
python manage.py shell -c "\
from django.contrib.auth import get_user_model; \
User = get_user_model(); \
User.objects.create_superuser('admin', 'admin@example.com', 'admin') \
if not User.objects.filter(username='admin').exists() else None"

# Démarrage serveur
exec python manage.py runserver 0.0.0.0:8000