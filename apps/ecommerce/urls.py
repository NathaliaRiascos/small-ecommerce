from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('acerca/', acerca, name='acerca'),
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
    path('contacto/', contacto, name='contacto'),
    path('carrito/', carrito, name='carrito')
]
