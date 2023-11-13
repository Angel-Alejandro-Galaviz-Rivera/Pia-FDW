from django.db import models

# Create your models here.
class Sucursales(models.Model):
    Id_Sucursal = models.IntegerField()
    Nombre = models.CharField(max_length=60)
    Ubicacion = models.CharField(max_length=60)
    Numero_de_Telefono = models.CharField(max_length=60)

