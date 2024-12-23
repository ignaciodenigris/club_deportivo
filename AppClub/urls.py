from django.urls import path

from AppClub.views import *

urlpatterns = [
    path('inicio/', inicio, name="inicio"),
    path('inscripcion/', inscripcion, name="inscripcion"),
    path('profesores/', SolicitudProfesor, name="profesores"),
    path('copetencias/', SolicitudCompetencia, name="copetencias"),
    path('forms/', tabla, name="forms"),
    path('formsProf/', tablaProfes, name = "formsProf"),
    path('formsComp/', tablaCompetencia, name = "formsComp"),
]