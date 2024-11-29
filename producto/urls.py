from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='productos'),
    path('productos/', views.lista_productos, name='lista_productos'),
    
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('productos/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('productos/ocultar/<int:producto_id>/', views.ocultar_producto, name='ocultar_producto'),
]
