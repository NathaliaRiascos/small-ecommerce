from django.urls import path, re_path
from django.views.static import serve
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('acerca/', acerca, name='acerca'),
    path('login/', user_login,  name='login'),
    path('logout/', LogoutView.as_view(),  name='logout'),
    path('registro/', registro, name='registro'),
    path('contacto/', contacto, name='contacto'),
    path('carrito/', login_required(carrito), name='carrito'),
    path('agregar_a_carrito/<int:producto_id>/<cantidad>', login_required(agregarACarrito), name="agregar_a_carrito"),
    path('eliminar_de_carrito/<int:id>/', login_required(eliminarDeCarrito), name="eliminar_de_carrito"),
    path('eliminar_carrito/', login_required(eliminarCarrito), name='eliminar_carrito')
]
 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)