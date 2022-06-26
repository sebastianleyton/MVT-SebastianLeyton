from django.db import models

# Create your models here.




class Familiar(models.Model):
    cedula_identidad = models.IntegerField()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()