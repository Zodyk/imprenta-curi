from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from django.shortcuts import get_object_or_404
import json
from producto.models import Producto  # Asegúrate de importar el modelo de producto
from decimal import Decimal
from producto.models import Producto
from django.shortcuts import render


def agregar_al_carrito(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # Cargar los datos enviados en la solicitud
        producto_id = data.get('producto_id')

        if not producto_id:
            return JsonResponse({'success': False, 'message': 'No se proporcionó el ID del producto'}, status=400)

        # Obtener el producto
        producto = get_object_or_404(Producto, id=producto_id)

        # Inicializar el carrito si no existe en la sesión
        carrito = request.session.get('carrito', {})

        # Agregar o actualizar el producto en el carrito
        if producto_id in carrito:
            carrito[producto_id]['cantidad'] += 1
        else:
            carrito[producto_id] = {
                'nombre': producto.nombre,
                'precio': str(producto.precio),  # Convertir Decimal a String
                'cantidad': 1,
                'imagen': producto.imagen.url if producto.imagen else "",
            }

        # Guardar el carrito en la sesión
        request.session['carrito'] = carrito
        print("Carrito actual:", request.session.get('carrito', {}))

        return JsonResponse({'success': True, 'message': 'Producto agregado al carrito'})

    return JsonResponse({'success': False, 'message': 'Método no permitido'}, status=405)

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    subtotal = 0
    envio = 7000  # Envío fijo en pesos chilenos

    # Calcular subtotal sumando precio * cantidad de cada producto
    for producto_id, datos in carrito.items():
        subtotal += float(datos['precio']) * datos['cantidad']

    # Calcular total
    total = subtotal + envio

    return JsonResponse({
        'carrito': carrito,
        'subtotal': round(subtotal, 2),
        'envio': envio,
        'total': round(total, 2),
    })


# Actualizar cantidad de producto en el carrito
def actualizar_carrito(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        producto_id = str(data.get('producto_id'))
        nueva_cantidad = data.get('cantidad')

        if producto_id in request.session['carrito']:
            if nueva_cantidad > 0:
                request.session['carrito'][producto_id]['cantidad'] = nueva_cantidad
            else:
                del request.session['carrito'][producto_id]
            request.session.modified = True
            return JsonResponse({'success': True, 'carrito': request.session['carrito']})
    return JsonResponse({'success': False, 'message': 'Error al actualizar el carrito'})

# Eliminar producto del carrito
def eliminar_del_carrito(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        producto_id = str(data.get('producto_id'))

        if producto_id in request.session['carrito']:
            del request.session['carrito'][producto_id]
            request.session.modified = True
            return JsonResponse({'success': True, 'carrito': request.session['carrito']})
    return JsonResponse({'success': False, 'message': 'Error al eliminar el producto del carrito'})

