from django.shortcuts import render
from django.db.models import Q
from apps.producto.models import * 

def buscador(request):
    queryset = request.GET.get('buscar')
    productos = Producto.objects.filter()
    if queryset: 
        productos = Producto.objects.filter(
            Q(titulo__icontains = queryset) | 
            Q(descripcion__icontains  = queryset)
        ).distinct() 
             
        return productos
    
def productosHome(request):
    last_products = Producto.objects.filter(estado = True).order_by('-id')[:3]
    products = Producto.objects.filter(estado = True).order_by('-id')[3:]
    context = { 
        'last_products': last_products,
        'products': products
    } 
    return context

def getProductos(request):
    products = Producto.objects.filter(estado = True)  
    context = { 'productos': products }
    return context


def getProducto(request):
    data = {
        'titulo': request.POST.get('titulo'),
        'slug': request.POST.get('slug'),
        'descripcion': request.POST.get('descripcion'),
        'precio': request.POST.get('precio'),
        'categoria': Categoria.objects.get(nombre= request.POST.get('categoria')),
    }
    
    return data