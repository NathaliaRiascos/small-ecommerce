from django.shortcuts import render, get_object_or_404,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .helper import buscador, getProductos, getProducto
from apps.ecommerce.models import Usuario
from .forms import *
from .models import *

def productos(request):     
    context = getProductos(request)
    respuesta = buscador(request)
    if respuesta: 
        context = { 'productos': respuesta  }
    return render(request, 'productos.html', context)
    

def detalleProducto(request,slug):
    try:
        product = Producto.objects.get(slug = slug)
        if request.method == 'GET': 
            context = { 'product': product }
            return render(request, 'producto.html', context)
        else: 
            return redirect('ecommerce:agregar_a_carrito', 
                producto_id= product.id,
                cantidad= request.POST.get('cantidad')
            )           
    except Producto.DoesNotExist:
        messages.add_message(
            request, messages.INFO, 
            f'Se encontro ningun producto con el slug: {slug}'
        )     
        if request.user.is_staff:    
            return redirect('producto:productos')
        else:
            return redirect('ecommerce:home')

def productosPorCategoria(request, nombre):
    productos = None   
    productos = buscador(request)    
    if productos:
        context = { 'productos': productos } 
        return render(request, 'productos.html', context) 
    
    # Filtrar producto de acuerdo a su categoria
    if request.method == 'GET':
        productos = Producto.objects.filter(
            estado = True, 
            categoria = Categoria.objects.get(nombre__iexact = nombre)
        )
        
    context = { 'productos': productos } 
    return render(request, 'productos.html', context)


def crearProducto(request):
    #Buscador
    productos = buscador(request)
    if productos:
        context = { 
            'productos': productos
        } 
        return render(request, 'productos.html', context)
    
    #Crear nuevo producto
    if request.method == 'POST':
        data = getProducto(request)
        producto = ProductoForm(data, request.FILES)

        if producto.is_valid():
            producto.save()
            return redirect('producto:productos')
        else: 
            print(producto.errors.as_json())            
    return render(request, 'staff/newproducto.html')



def editarProducto(request, id):    
    product = Producto.objects.filter(estado= True, id = id).first()   
    context = {
        'product': product,
        'imagen': request.FILES
    }
    
    if request.method == 'POST':
        data = getProducto(request)
        producto = ProductoForm(data, request.FILES,instance= product)
        
        if producto.is_valid():
            producto.save()
            return redirect('producto:productos')
        else:
            print(producto.errors.as_json())
    return render(request, 'staff/producto.html', context)
    

def eliminarProducto(request, id):
    producto = Producto.objects.get(id = id)
    if request.method == 'POST':
        producto.estado = False
        producto.save()
        return redirect('producto:productos')
    
    return render(request, 'staff/eliminarProducto.html', {'product': producto})

