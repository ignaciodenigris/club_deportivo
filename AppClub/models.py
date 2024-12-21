from django.db import models

class Inscripcion(models.Model):
    nombre = models.CharField(max_length=100) 
    apellido = models.CharField(max_length=30)
    deporte = models.CharField(max_length=30)

class Profesor(models.Model):
    nombre = models.CharField(max_length=30) 
    apellido = models.CharField(max_length=30) 
    email = models.EmailField() 
    profesion = models.CharField(max_length=50)  

class Copetencias(models.Model):
    nombre = models.CharField(max_length=100)
    deporte = models.CharField(max_length=30)
    fechaDeCopetencia = models.DateField()  
    entregado = models.BooleanField() 

# Create your models here.
