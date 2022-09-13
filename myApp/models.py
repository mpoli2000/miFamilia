from django.db import models

# Create your models here.
class FamilyDB(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    edad = models.IntegerField()
    estado = models.BooleanField()