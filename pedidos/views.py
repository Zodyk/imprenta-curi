
from producto.models import Producto
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.utils.timezone import now
from pedidos.models import Pedido, PedidoProducto
from usuarios.models import Usuario
from datetime import datetime
from django.contrib import messages
from django.utils import timezone


@login_required
def checkout(request):
    if request.method == 'POST':
        carrito = request.session.get('carrito', {})
        if not carrito:
            return JsonResponse({'error': 'El carrito está vacío'}, status=400)

        total = 0
        pedido = Pedido.objects.create(usuario=request.user, fecha=now())

        for producto_id, item in carrito.items():
            producto = Producto.objects.get(id=producto_id)
            cantidad = item['cantidad']
            PedidoProducto.objects.create(pedido=pedido, producto=producto, cantidad=cantidad)
            total += producto.precio * cantidad

        pedido.total = total
        pedido.save()

        # Vaciar el carrito
        request.session['carrito'] = {}
        return JsonResponse({'success': 'Pedido realizado correctamente', 'pedido_id': pedido.id})

    return JsonResponse({'error': 'Método no permitido'}, status=405)

@login_required
def procesar_compra(request):
    if request.method == 'POST':
        usuario = request.user
        carrito = request.session.get('carrito', {})

        if not carrito:
            return JsonResponse({'success': False, 'message': 'El carrito está vacío.'})

        total = sum(float(item['precio']) * item['cantidad'] for item in carrito.values())

        # Crear el pedido
        pedido = Pedido.objects.create(
            cliente=usuario,
            fecha=timezone.now(),
            total=total
        )

        # Agregar los productos al pedido
        for producto_id, item in carrito.items():
            producto = Producto.objects.get(id=producto_id)
            PedidoProducto.objects.create(
                pedido=pedido,
                producto=producto,
                cantidad=item['cantidad']
            )

        # Vaciar el carrito
        request.session['carrito'] = {}
        request.session.modified = True

        return JsonResponse({'success': True, 'message': 'Compra realizada con éxito.', 'pedido_id': pedido.id})

    return JsonResponse({'success': False, 'message': 'Método no permitido.'})
