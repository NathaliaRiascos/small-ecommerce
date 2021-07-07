from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('', productos, name="productos"),
    path('categoria/<nombre>/', productosPorCategoria, name="categoria"),
    path('crear_producto/', login_required(crearProducto), name='crear_producto'),
    path('editar_producto/<int:id>/', login_required(editarProducto), name="editar_producto"),
    path('eliminar_producto/<int:id>/', login_required(eliminarProducto), name="eliminar_producto"),
    path('<slug:slug>/', detalleProducto, name='detalle_producto'),
]
'''
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT
    }),
    
]'''
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)