from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from backend.forms import RegisterForm
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html', {
        'title': 'titulo de la pagina'
    })
    
def about(request):
    return render(request, 'mainapp/about.html', {
        'title': "Sobre nosotros"
    })
    
def register_page(request):
    
    register_form = RegisterForm()

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        
        if register_form.is_valid():    
            register_form.save()
            messages.success(request, 'Te has registrado correctamente')
            
    else:
        register_form = RegisterForm()
    
    return render(request, 'users/register.html', {
        'title': 'Registro',
        'register_form': register_form
    })
    
    
def login_page(request):
    
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        
        orlin = User.objects.filter(pk=user.id)

        data = []
    
        for usuario in orlin:
            data.append({
                "username": usuario.username,
                'password': usuario.password
            })
        
        print(data)
        return JsonResponse(data, safe=False)
    
    else:
        messages.warning(request, 'No Te has identificado correctamente')
    
    return render(request, 'users/login.html', {
        'login': 'Login'
    })
    
def logout_user(request):
    logout(request)
    return redirect('login')