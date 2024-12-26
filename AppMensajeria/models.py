from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
    remitente = models.ForeignKey(User, related_name="mensaje_enviados", on_delete=models.CASCADE) 
    destinatario = models.ForeignKey(User, related_name="mensaje_recibidos", on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Mensaje de: {self.remitente} a {self.destinatario}"
# Create your models here.
