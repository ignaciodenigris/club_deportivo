from django.db import models

class Inscripcion(models.Model):
    nombre = models.CharField(max_length=100) 
    apellido = models.CharField(max_length=30)
    deporte = models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre} -- Apellido: {self.apellido} -- Deporte: {self.deporte}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=30) 
    apellido = models.CharField(max_length=30) 
    email = models.EmailField() 
    profesion = models.CharField(max_length=50)  
    def __str__(self):
        return f"Nombre: {self.nombre} -- Apellido: {self.apellido} -- email: {self.email} -- especialidad:{self.profesion}"


class Copetencias(models.Model):
    nombre = models.CharField(max_length=100)
    deporte = models.CharField(max_length=30)
    fecha = models.DateField()  
    def __str__(self):
        return f"Nombre: {self.nombre} -- Apellido: {self.apellido} -- Fecha de la Copetencia: {self.fecha}"

# Create your models here.
