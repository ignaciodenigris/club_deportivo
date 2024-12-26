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
    
    
    path('alumno_form/', alumno_form, name = "alumno_form"),
    path('profesor_form/', profesor_form, name = "profesor_form"),
    path('competencias_form/', competencias_form, name = "competencias_form"),
    
    
    
    path('correct_edit/', correct_edit, name = "correct_edit"),
    
    
    
    path('eliminar_solicAlumno/<int:id>', eliminar_solicAlumno, name = "eliminar_solicAlumno"),
    path('edit_solicAlumno/<int:id>', edit_solicAlumno, name = "edit_solicAlumno"),
    path('eliminar_solicProfe/<int:id>', eliminar_solicProfe, name = "eliminar_solicProfe"),
    path('edit_solicProfe/<int:id>', edit_solicProfe, name = "edit_solicProfe"),
    path('eliminar_soliComp/<int:id>', eliminar_soliComp, name = "eliminar_soliComp"),
    path('edit_soliComp/<int:id>', edit_soliComp, name = "edit_soliComp"),
    
]