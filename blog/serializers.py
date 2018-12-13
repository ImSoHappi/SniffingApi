from .models import Cliente,Empleado,Orden,Usuario
from rest_framework import serializers

class ClienteSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model= Cliente
        fields = ( 'id', 'nombre', 'direccion', 'ciudad', 'comuna', 'telefono', 'correo' )


class EmpleadoSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Empleado
        fields = ('rut','nombre','telefono','correo','cliente')

class OrdenSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Orden
        fields= ('folio','cliente','fecha','horainicio','horatermino','idascensor','modelo','fallas','reparaciones','piezas','trabajador')

class UsuarioSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Usuario
        fields= ('usuario','contraseña')