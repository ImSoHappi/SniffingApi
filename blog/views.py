from .models import Cliente
from django.shortcuts import render
from rest_framework import viewsets
from blog.serializers import ClienteSerializer

class ClienteViewSet( viewsets.ModelViewSet ):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
