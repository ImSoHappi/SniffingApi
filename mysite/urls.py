from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from blog import views

router = routers.DefaultRouter( )
router.register( r'clientes', views.ClienteViewSet )
router.register(r'Empleados',views.EmpleadoViewSet)
router.register(r'Orden',views.OrdenViewSet)
router.register(r'Usuario',views.UsuarioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url( r'^', include( router.urls ) ),
    url( r'^api-auth/', include( 'rest_framework.urls', namespace='rest'))
]
