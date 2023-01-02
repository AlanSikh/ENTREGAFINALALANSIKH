from django.db import models

# Create your models here.
class Curso(models.Model):
    curso=models.CharField(max_length=40)
    camada=models.IntegerField(unique=True)
    numero_dia=models.IntegerField()

class Profesor(models.Model):
    nombre=models.CharField(max_length=40)
    email=models.EmailField()
    DNI=models.BigIntegerField() 

class Alumno(models.Model):
    nombre=models.CharField(max_length=40)  
    email=models.EmailField()
    DNI=models.BigIntegerField()   