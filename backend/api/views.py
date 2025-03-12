from rest_framework import generics
from .models import ContactMessage, Devis, CustomUser
from .serializers import ContactSerializer, DevisSerializer, UserSerializer
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class ContactCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactSerializer

class DevisCreateView(generics.CreateAPIView):
    queryset = Devis.objects.all()
    serializer_class = DevisSerializer

class DevisListView(generics.ListAPIView):
    serializer_class = DevisSerializer
    
    def get_queryset(self):
        return Devis.objects.filter(user=self.request.user)