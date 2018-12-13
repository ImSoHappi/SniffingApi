from django.contrib import admin
from .models import Cliente, Orden, Empleado,Usuario

admin.site.register( Cliente )
admin.site.register (Orden)
admin.site.register ( Empleado)
admin.site.register (Usuario)
