from django.urls import path
from . import views
from pedidos import views as pedidos_views
from .views import procesar_compra

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('procesar-compra/', pedidos_views.procesar_compra, name='procesar_compra'),
    path('procesar-compra/', procesar_compra, name='procesar_compra'),
    
]
