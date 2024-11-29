from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from producto.models import Producto
from django.contrib import messages

# Verificar si el usuario es administrador
def es_admin(user):
    return user.is_staff or user.is_superuser

@user_passes_test(es_admin)
def modificar_productos(request):
    if request.method == "POST":
        productos = Producto.objects.all()
        for producto in productos:
            producto.nombre = request.POST.get(f'nombre_{producto.id}')
            producto.sku = request.POST.get(f'sku_{producto.id}')
            producto.descripcion = request.POST.get(f'descripcion_{producto.id}')
            producto.precio = request.POST.get(f'precio_{producto.id}')
            producto.stock = request.POST.get(f'stock_{producto.id}')
            producto.categoria = request.POST.get(f'categoria_{producto.id}')
            producto.visible = request.POST.get(f'visible_{producto.id}') == 'on'
            
            # Manejar imagen
            if f'imagen_{producto.id}' in request.FILES:
                producto.imagen = request.FILES[f'imagen_{producto.id}']
            
            producto.save()

        return redirect('modificar')  # Redirige a la misma página después de guardar

    productos = Producto.objects.all()
    return render(request, 'modificar.html', {'productos': productos})




def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        imagen = request.FILES.get('imagen')
        sku = request.POST.get('sku')
        descripcion = request.POST.get('descripcion', '')
        stock = request.POST.get('stock')
        precio = request.POST.get('precio')
        categoria = request.POST.get('categoria')
        visible = 'visible' in request.POST

        Producto.objects.create(
            nombre=nombre,
            imagen=imagen,
            sku=sku,
            descripcion=descripcion,
            stock=stock,
            precio=precio,
            categoria=categoria,
            visible=visible
        )
        messages.success(request, 'Producto creado exitosamente.')
        return redirect('modificar')

