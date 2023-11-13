from django.db import models

# Create your models here.
class Departamentos(models.Model):
    Id_Departamento = models.IntegerField()
    Nombre = models.CharField(max_length=60)
    Descripcion = models.CharField(max_length=60)
    Responsable = models.CharField(max_length=60)

