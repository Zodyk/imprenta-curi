# Generated by Django 5.1.1 on 2024-11-25 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_address_usuario_country_usuario_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='country',
            field=models.CharField(blank=True, default='chile', max_length=100),
        ),
    ]
