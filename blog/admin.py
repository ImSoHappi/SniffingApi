from django.contrib import admin
from .models import Cliente, Orden, Empleado

admin.site.register( Cliente )
admin.site.register (Orden)
admin.site.register ( Empleado)