# Generated by Django 5.1.1 on 2024-11-29 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_alter_pedido_fecha_alter_pedido_usuario_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='usuario',
            new_name='cliente',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='productos',
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
