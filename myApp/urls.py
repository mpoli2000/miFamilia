from django.urls import path
from myApp.views import *

urlpatterns = [
    path('', inicio),
    path('ingresar', ingresar),
    path('listar', listar),
]