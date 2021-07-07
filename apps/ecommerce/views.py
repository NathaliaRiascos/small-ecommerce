from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import Usuario
from apps.producto.models import * 
from apps.producto.helper import *


def home(request):
    #Buscador
    productos = buscador(request)
    if productos:
        context = { 'productos': productos } 
        return render(request, 'productos.html', context)
    
    if request.user.is_staff:   
        return redirect('producto:productos')
    
    context = productosHome(request)
    
    return render(request, 'home.html', context)


def menu(request):
    categorias = Categoria.objects.filter(estado = True)  
    context = { 'categorias': categorias }
    return context
   

def user_login(request): 
    # Buscador
    productos = buscador(request)   
    if productos:
        context = { 'productos': productos } 
        return render(request, 'productos.html', context) 
    
    #Logica de login
    if request.method == 'POST':    
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)

        context = None
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('producto:productos')
            else:
                return redirect('ecommerce:home')
          
    return render(request, 'login.html')

def registro(request): 
    # Buscador
    productos = buscador(request)
    if productos:
        context = { 
            'productos': productos
        } 
        return render(request, 'productos.html', context)
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repeat_password = request.POST.get('password2')
        
        if password == repeat_password:
            user = Usuario.objects.create_user(email, username, password)
            user = authenticate(request, username=email, password=password)
            login(request, user)
            
            return redirect('ecommerce:home')

    return render(request, 'registro.html')


def acerca(request):  
    #Buscador 
    productos = buscador(request)
    if productos:
        context = { 'productos': productos } 
        return render(request, 'productos.html', context)
    
    return render(request, 'acerca.html')


def contacto(request):
    productos = buscador(request)
    
    if productos:
        context = { 
            'productos': productos
        } 
        return render(request, 'productos.html', context)
    
    return render(request, 'contacto.html')

def carrito(request):
    # Buscador
    productos = buscador(request)  
    if productos:
        context = { 'productos': productos } 
        return render(request, 'productos.html', context)
    
    usuario = Usuario.objects.get(id = request.user.id)
    carrito = Carrito.objects.get(usuario = usuario)   
    productos = carrito.producto.all()
    
    if not productos:
        carrito.total = 0
        
    context = {
        'productos': productos,
        'total': carrito.total
    }
    return render(request, 'carrito.html', context)


def agregarACarrito(request, producto_id,cantidad): 
    usuario = Usuario.objects.get(id = request.user.id)
    producto = Producto.objects.get(id = producto_id)
    
    # ARREGLAR TOTAL
    try:
        carrito = Carrito.objects.get(usuario = usuario)

        if not producto in carrito.producto.all():
            producto.precio =  float(producto.precio) * int(cantidad)
            carrito.producto.add(producto)
            carrito.total += float(producto.precio)
        else:
            print('Ya existe')
        carrito.save()
    except Carrito.DoesNotExist:
        carrito = Carrito.objects.create(usuario = usuario)
        carrito.total = 0
        if not producto in carrito.producto.all():
            producto.precio =  float(producto.precio) * int(cantidad)
            carrito.producto.add(producto)
            carrito.total += float(producto.precio)      
        carrito.save()
    
    return redirect('ecommerce:carrito')

    
def eliminarDeCarrito(request, id):
    producto = Producto.objects.get(id = id)
    usuario = Usuario.objects.get(id = request.user.id)
    carrito = Carrito.objects.get(usuario = usuario)
    
    if request.method == 'POST':
        if producto in carrito.producto.all():
            carrito.producto.remove(producto)
            carrito.total -= float(producto.precio)
        carrito.save()
        return redirect('ecommerce:carrito')
    
    return render(request, 'staff/eliminarProducto.html', {'product': producto})
    
    
def eliminarCarrito(request):  
    usuario = Usuario.objects.get(id = request.user.id)
    carrito = Carrito.objects.get(usuario = usuario)  
    carrito.producto.clear()
    
    return redirect('ecommerce:carrito')
    