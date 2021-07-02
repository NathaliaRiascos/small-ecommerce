from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
from .models import Usuario

# Create your views here.
def home(request):
    return render(request, 'home.html')

def user_login(request):
    
    if request.method == 'POST':
        
        email = request.POST.get('email')
        password = request.POST.get('password')        
        print(email, password)
        user = authenticate(request, username=email, password=password)
        print('Antes de loguearse', user)
        
        if user is not None:
            login(request, user)
            
            if user.is_staff:
                return render(request, 'productos.html')

            
    return render(request, 'login.html')

def registro(request):
     
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repeat_password = request.POST.get('password2')
        
        if password == repeat_password:
            
            user = Usuario.objects.create_user(email, username, password)

    return render(request, 'registro.html')


def acerca(request):
    return render(request, 'acerca.html')

def contacto(request):
    return render(request, 'contacto.html')

def carrito(request):
    return render(request, 'carrito.html')


