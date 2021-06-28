from django.shortcuts import render

# Create your views here.

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