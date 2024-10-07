from django.db import models
from django.contrib.auth.models import User


class Vehiculo(models.Model):
  # Opciones por Marca
  MARCA = (
      ('FIAT', 'Fiat'),
      ('FORD', 'Ford'),
      ('CHEVROLET', 'Chevrolet'),
      ('TOYOTA', 'Toyota'),
  )
  # Opciones por Marca
  CATEGORIA = (
      ('PARTICULAR', 'Particular'),
      ('TRASPORTE', 'Transporte'),
      ('CARGA', 'Carga'), 
  )

    # Campos del modelo
  marca = models.CharField(max_length=20, choices=MARCA, default='FORD')
  modelo = models.CharField(max_length=100)
  serial_carroceria = models.CharField(max_length=50)
  serial_motor = models.CharField(max_length=50)
  categoria = models.CharField(max_length=20, choices=CATEGORIA, default='PARTICULAR')
  precio = models.FloatField()
  f_creacion = models.DateTimeField(auto_now_add=True)
  f_modificado = models.DateTimeField(auto_now = True)

  class Meta:
     permissions = ( ("vizualizar_catalogo", "Visualizar Catalogo de Vehiculos"),)

  def __str__(self):
      return self.modelo
