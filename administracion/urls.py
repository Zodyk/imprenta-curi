from django.urls import path
from . import views

urlpatterns = [
    path('modificar/', views.modificar_productos, name='modificar'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),

]
