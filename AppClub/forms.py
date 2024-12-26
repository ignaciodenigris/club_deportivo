from django import forms
from AppClub.models import Inscripcion, Profesor, Copetencias

class AlumnoFormulario(forms.ModelForm):
    class Meta: 
        model = Inscripcion 
        fields = "__all__"

class ProfesorFormulario(forms.ModelForm):
    class Meta: 
        model = Profesor 
        fields = "__all__"
        
class CompetenciasFormulario(forms.ModelForm):
    class Meta: 
        model = Copetencias 
        fields = "__all__"