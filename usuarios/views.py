from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import Usuario

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from pedidos.models import Pedido, PedidoProducto
from django.http import JsonResponse

# Vista para el registro de usuarios
def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = make_password(request.POST['password'])  # Encripta la contraseña

        # Verificar si el correo ya existe
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Este correo ya está registrado.')
            return render(request, 'login.html')  # Devuelve la página con el mensaje de error

        # Crear el usuario si el correo no existe
        Usuario.objects.create(username=username, email=email, password=password)
        messages.success(request, 'Usuario registrado exitosamente. Inicia sesión.')
        return redirect('login')  # Redirige al login después del registro

    return render(request, 'login.html')

# Vista para el login

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True, 'redirect': '/perfil/'})
        else:
            return JsonResponse({'success': False, 'message': 'Correo o contraseña incorrectos.'})

    return render(request, 'login.html')

def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('index')  # Redirige a la página de inicio

# Vista para el perfil del usuario


@login_required
def perfil(request):
    usuario = request.user
    # Obtiene todos los pedidos del usuario ordenados por fecha descendente
    pedidos = Pedido.objects.filter(cliente=usuario).order_by('-fecha')

    # Generar una lista con la información de cada pedido
    pedidos_con_productos = []
    for pedido in pedidos:
        # Asegúrate de obtener los productos relacionados con este pedido
        productos = PedidoProducto.objects.filter(pedido=pedido)
        detalles_productos = ", ".join(
            [f"{pp.producto.nombre} (x{pp.cantidad})" for pp in productos]
        )

        pedidos_con_productos.append({
            'id': pedido.id,
            'fecha': pedido.fecha,
            'total': pedido.total,
            'productos': detalles_productos,  # Nombres y cantidades de los productos
        })

    # Renderizar la plantilla con los pedidos actualizados
    return render(request, 'perfil.html', {
        'usuario': usuario,
        'pedidos': pedidos_con_productos,
    })





@login_required
def perfil_general(request):
    if request.method == 'POST':
        # Depurar datos enviados por el formulario
        print("Datos recibidos del formulario:", request.POST)

        # Recuperar usuario autenticado
        user = request.user

        # Actualizar campos editables
        user.username = request.POST.get('username')  # Nombre
        user.last_name = request.POST.get('last_name')  # Apellido
        user.country = request.POST.get('country')  # País
        user.address = request.POST.get('address')
        user.phone = request.POST.get('phone')  # Teléfono

        # Guardar cambios
        try:
            user.save()
            messages.success(request, 'Tus datos han sido actualizados correctamente.')
        except Exception as e:
            messages.error(request, f'Error al actualizar: {e}')

        # Redirigir al perfil después de guardar cambios
        return redirect('perfil')

    # Renderizar datos actuales en el perfil
    return render(request, 'perfil.html', {'usuario': request.user})


from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password

from django.http import JsonResponse

@login_required
def cambiar_contrasena(request):
    if request.method == 'POST':
        user = request.user
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # Validar contraseña actual
        if not check_password(current_password, user.password):
            return JsonResponse({'success': False, 'message': 'La contraseña actual es incorrecta.'})

        # Validar que las contraseñas nuevas coincidan
        if new_password != confirm_password:
            return JsonResponse({'success': False, 'message': 'Las contraseñas nuevas no coinciden.'})

        # Cambiar contraseña
        user.set_password(new_password)
        user.save()

        # Mantener la sesión del usuario activa
        update_session_auth_hash(request, user)

        return JsonResponse({'success': True, 'message': 'Tu contraseña ha sido cambiada exitosamente.'})

    return JsonResponse({'success': False, 'message': 'Método no permitido.'})

