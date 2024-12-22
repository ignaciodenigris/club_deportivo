from django.urls import path

from AppClub.views import *

urlpatterns = [
    path('inicio/', inicio, name="inicio"),
    path('inscripcion/', inscripcion, name="inscripcion"),
    path('forms/', tabla, name="forms"),
]