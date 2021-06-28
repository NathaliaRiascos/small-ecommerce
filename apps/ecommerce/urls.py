from django.urls import path
from .views import *


urlpatterns = [
    path('', productos, name="productos"),
    path('detalle_producto/', detalleProducto, name='detalle_producto'),
    path('crear_producto/', crearProducto, name='crear_producto')
]
