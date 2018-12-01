from .models import Cliente
from rest_framework import serializers

class ClienteSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model= Cliente
        fields = ( 'nombre', 'direccion', 'ciudad', 'comuna', 'telefono', 'correo' )

