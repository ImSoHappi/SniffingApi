from .models import Cliente,Empleado,Orden
from django.shortcuts import render
from rest_framework import viewsets
from blog.serializers import ClienteSerializer,EmpleadoSerializer, OrdenSerializer

class ClienteViewSet( viewsets.ModelViewSet ):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class EmpleadoViewSet (viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class OrdenViewSet (viewsets.ModelViewSet):
    queryset= Orden.objects.all()
    serializer_class= OrdenSerializer