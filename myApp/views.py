from django.shortcuts import render
from django.http import HttpResponse
from .models import FamilyDB

# Create your views here.
def inicio(request):
    return render(request,'inicio.html')

def ingresar(request):
    datos = {'nombre': 'Martin', 
    'apellido': 'Poli', 
    'email': 'martin@gmail.com', 
    'created_at': '13/09/2022',
    'updated_at': '13/09/2022',
    'edad': 51,
    'estado': True
    }
    return render(request, 'ingresar.html')

def listar(request):
    datos = FamilyDB.objects.all()
    for dato in datos:
        print(dato.nombre)

    return render(request, 'listar.html', {'datos': datos})