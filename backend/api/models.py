from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255)

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Devis(models.Model):
    STATUS_CHOICES = [('draft', 'Brouillon'), ('sent', 'Envoyé')]
    
    provider = models.JSONField()
    recipient = models.JSONField()
    project = models.JSONField()
    total_ttc = models.DecimalField(max_digits=10, decimal_places=2)
    payment_phases = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)