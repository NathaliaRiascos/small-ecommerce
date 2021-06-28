from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def registro(request):
    return render(request, 'registro.html')

def acerca(request):
    return render(request, 'acerca.html')

def contacto(request):
    return render(request, 'contacto.html')

def productos(request):
    return render(request, 'productos.html', {
        'producto': 'Hola'
    })
    
def detalleProducto(request):
    return render(request, 'producto/producto.html')

def crearProducto(request):
    '''if request.method == 'POST':
        print(request.POST)'''
        
    return render(request, 'producto/newproducto.html')