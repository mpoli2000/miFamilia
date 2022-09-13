from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request,'inicio.html')

def ingresar(request):
    datos = {'nombre': 'Martin', 
    'apellido': 'Poli', 
    'email': 'martin@gamil.com', 
    'fecha_nacimiento': None,
    'edad': 0,
    'estado': True
    }
    return render(request, 'ingresar.html')

def listar(request):
    return render(request, 'listar.html')