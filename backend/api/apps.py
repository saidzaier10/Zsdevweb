from django.apps import AppConfig

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'  # Doit correspondre exactement au nom du module Python
    label = 'api'  # Conserver le label original