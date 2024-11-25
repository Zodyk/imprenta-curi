from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/general/', views.perfil_general, name='perfil_general'), 
    path('perfil/cambiar-contrasena/', views.cambiar_contrasena, name='cambiar_contrasena'),
]
