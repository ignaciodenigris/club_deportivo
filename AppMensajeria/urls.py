from django.urls import path

from AppMensajeria.views import *

urlpatterns = [
    path('enviar_mensaje/', enviar_mensaje, name="enviar_mensaje"),
    path('mostrar_mensajes/', mostrar_mensajes, name="mostrar_mensajes"),
]