from django import forms
from AppClub.models import Inscripcion, Profesor, Copetencias, Profile
from django.contrib.auth.models import User

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

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name","email")

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("photo",)

