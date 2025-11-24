from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Contacto
from .serializers import ContactoSerializer

class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all().order_by('-fecha_creacion')
    serializer_class = ContactoSerializer#modo invitado sin token
    permission_classes = [IsAuthenticatedOrReadOnly]