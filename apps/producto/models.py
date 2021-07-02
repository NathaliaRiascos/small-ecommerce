from django.db import models
from apps.ecommerce.models import * 

# Create your models here.
'''
Categorias:
o Descripcion
• Productos:
o Titulo
o Imagen
o Descripcion
o Precio
o Categoria a la que pertenece
• Carrito:
o Usuario
o Lista de productos del usuario.
o Total del carrito
'''

class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de la categoria', max_length= 100 , null = False, blank = False)
    estado = models.BooleanField('Categoria Activada/Categoria no activada', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorias'
        
    def __str__(self):
        return self.nombre
    
    
class Producto(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Título', max_length = 90, blank = False, null = False)
    slug = models.SlugField('Slug', max_length = 100, blank = False, null = False)
    descripcion = models.CharField('Descripción', max_length = 110, blank = False, null = False)
    precio = models.FloatField('precio', max_length = 100, blank = False, null = False)
    imagen = models.ImageField('Imagen de producto', upload_to='img_product/', height_field=None, width_field=None, max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    estado = models.BooleanField('Activo/No activo', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        
    def __str__(self):
        return self.titulo
    
    
class Carrito(models.Model):
    usuario =  models.OneToOneField(Usuario, on_delete = models.CASCADE)
    producto = models.ManyToManyField(Producto)
    total = models.FloatField(max_length = 100, blank = False, null = False, default = 0)
    
    class Meta:
        verbose_name = 'Carrito'
        verbose_name_plural = 'Carrito'
        
    def __str__(self):
        return f'{self.usuario.username}'

    