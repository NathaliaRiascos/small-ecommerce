from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Carrito)