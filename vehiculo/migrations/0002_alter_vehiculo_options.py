# Generated by Django 4.2.16 on 2024-10-04 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'permissions': (('vizualizar_catalogo', 'Visualizar Catalogo de Vehiculos'),)},
        ),
    ]
