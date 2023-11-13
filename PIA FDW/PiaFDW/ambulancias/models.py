from django.db import models

# Create your models here.
class Ambulancias(models.Model):
    Id_Ambulancia = models.IntegerField()
    Marca = models.CharField(max_length=60)
    Modelo = models.CharField(max_length=60)
    Estado = models.CharField(max_length=60)

