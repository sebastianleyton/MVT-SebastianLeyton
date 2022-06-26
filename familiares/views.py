from django.shortcuts import render
from .models import Familiar


# Create your views here.


# Clase Familiar
# cedula_identidad = models.IntegerField()
# nombre = models.CharField(max_length=30)
# apellido = models.CharField(max_length=30)
# fecha_nacimiento = models.DateField()

def camellosaurio(request):
    familiar_1 = Familiar(cedula_identidad=22345678, nombre='Josesito', apellido='Ninja', fecha_nacimiento='07/11/2000')
    familiar_2 = Familiar(cedula_identidad=32345678, nombre='Josesita', apellido='Samurai', fecha_nacimiento='04/10/1999')
    familiar_3 = Familiar(cedula_identidad=14345678, nombre='Camello', apellido='Metalico', fecha_nacimiento='04/01/1991')
    lista_familiares = [familiar_1, familiar_2, familiar_3]
    return render(request, 'index.html', {'lista_familiares': lista_familiares})
