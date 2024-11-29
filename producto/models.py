from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='productos/')  # Requiere configurar media en settings.py
    sku = models.CharField(max_length=100, unique=True)  # Código único
    descripcion = models.TextField(blank=True)
    stock = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)
    visible = models.BooleanField(default=True)  # Controla si el producto es visible en la tienda

    def __str__(self):
        return self.nombre
