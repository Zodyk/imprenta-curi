from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from usuarios import views

def index(request):
    return render(request, 'index.html')

def productos(request):
    return render(request, 'productos.html')

def servicios(request):
    return render(request, 'servicios.html')

def contacto(request):
    return render(request, 'contacto.html')

def login(request):
    return render(request, 'login.html')

def perfil(request):
    return render(request, 'perfil.html', {'usuario': request.user})
