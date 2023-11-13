from django.db import models

# Create your models here.
class Medicos(models.Model):
    Id_Medico = models.IntegerField()
    Nombre_Completo = models.CharField(max_length=60)
    Especialidad = models.CharField(max_length=60)
    Numero_de_Telefono = models.CharField(max_length=60)

