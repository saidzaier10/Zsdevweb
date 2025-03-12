from django.urls import path
from .views import contact_view, register_view, devis_view, devis_list_view
from django.contrib import admin

urlpatterns = [
    path('api/contact/', contact_view, name='contact'),
    path('api/register/', register_view, name='register'),
    path('api/devis/', devis_view, name='devis'),
    path('api/mes-devis/', devis_list_view, name='devis-list'),
    path('', views.index, name='index')
]
