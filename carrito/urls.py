from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('ver/', views.ver_carrito, name='ver_carrito'),
    path('actualizar/', views.actualizar_carrito, name='actualizar_carrito'),
    path('eliminar/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
]
