from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Producto
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Crear producto
def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        imagen = request.FILES['imagen']
        sku = request.POST['sku']
        descripcion = request.POST['descripcion']
        stock = int(request.POST['stock'])
        precio = float(request.POST['precio'])
        categoria = request.POST['categoria']

        Producto.objects.create(
            nombre=nombre, imagen=imagen, sku=sku,
            descripcion=descripcion, stock=stock, precio=precio, categoria=categoria
        )
        messages.success(request, 'Producto creado exitosamente.')
        return redirect('lista_productos')

    return render(request, 'crear_producto.html')


def lista_productos(request):
    productos = Producto.objects.filter(visible=True)  # Mostrar solo productos visibles
    return render(request, 'productos.html', {'productos': productos})


# Editar producto
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.descripcion = request.POST['descripcion']
        producto.stock = int(request.POST['stock'])
        producto.precio = float(request.POST['precio'])
        producto.categoria = request.POST['categoria']
        producto.visible = 'visible' in request.POST  # Checkbox
        if 'imagen' in request.FILES:
            producto.imagen = request.FILES['imagen']
        producto.save()
        messages.success(request, 'Producto actualizado exitosamente.')
        return redirect('lista_productos')

    return render(request, 'editar_producto.html', {'producto': producto})

# Ocultar producto (fuera de stock)
def ocultar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.visible = False
    producto.save()
    messages.success(request, 'Producto ocultado.')
    return redirect('lista_productos')


