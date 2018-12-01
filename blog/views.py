from .models import Cliente
from rest_framework import viewsets
from blog.serializers import ClienteSerializer

class ClienteViewSet( viewsets.ModelViewSet ):
    queryset = Cliente.objects.all().order_by( 'nombre' )
    serializer_class = ClienteSerializer
