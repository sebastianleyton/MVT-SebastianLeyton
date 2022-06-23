from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Prueba


# Create your views here.

def view(request):
    return render(request, 'index.html')


def template(request):

    prueba1 = Prueba(nombre='Carlos')
    prueba2 = Prueba(nombre='Ricardo')
    prueba3 = Prueba(nombre='Stuart')

    return render(request, 'mi_template.html', {'lista_objetos': [prueba1, prueba2, prueba3]})
