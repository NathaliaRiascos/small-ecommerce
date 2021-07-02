from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('acerca/', acerca, name='acerca'),
    path('login/', user_login,  name='login'),
    path('logout/', LogoutView.as_view(),  name='logout'),
    path('registro/', registro, name='registro'),
    path('contacto/', contacto, name='contacto'),
    path('carrito/', carrito, name='carrito')
]
 