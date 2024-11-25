"""
URL configuration for Imprentacuri project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views as main_views  # Vistas del proyecto principal
from usuarios import views as user_views  # Vistas de la aplicación usuarios

urlpatterns = [
    path('', main_views.index, name='index'),  # Vistas del proyecto principal
    path('productos/', main_views.productos, name='productos'),
    path('servicios/', main_views.servicios, name='servicios'),
    path('contacto/', main_views.contacto, name='contacto'),
    path('usuarios/', include('usuarios.urls')),  # Incluye las rutas de usuarios
    path('login/', user_views.login_view, name='login'),  # Login de la aplicación usuarios
    path('perfil/', user_views.perfil, name='perfil'),  # Perfil de la aplicación usuarios
    path('admin/', admin.site.urls),
]
