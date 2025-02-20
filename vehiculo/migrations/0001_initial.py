# Generated by Django 4.2.16 on 2024-10-04 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(choices=[('FIAT', 'Fiat'), ('FORD', 'Ford'), ('CHEVROLET', 'Chevrolet'), ('TOYOTA', 'Toyota')], default='FORD', max_length=20)),
                ('modelo', models.TextField(max_length=100)),
                ('serial_carroceria', models.TextField(max_length=50)),
                ('serial_motor', models.TextField(max_length=50)),
                ('categoria', models.CharField(choices=[('PARTICULAR', 'Particular'), ('TRASPORTE', 'Transporte'), ('CARGA', 'Carga')], default='PARTICULAR', max_length=20)),
                ('precio', models.FloatField()),
                ('f_creacion', models.DateTimeField(auto_now_add=True)),
                ('f_modificado', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
