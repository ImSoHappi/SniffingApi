from .models import Cliente,Empleado,Orden,Usuario
from django.shortcuts import render
from rest_framework import viewsets
from blog.serializers import ClienteSerializer,EmpleadoSerializer, OrdenSerializer,UsuarioSerializer

class ClienteViewSet( viewsets.ModelViewSet ):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class EmpleadoViewSet (viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class OrdenViewSet (viewsets.ModelViewSet):
    queryset= Orden.objects.all()
    serializer_class= OrdenSerializer

class UsuarioViewSet (viewsets.ModelViewSet):
    queryset= Usuario.objects.all()
    serializer_class= UsuarioSerializer