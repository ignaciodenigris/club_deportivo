from django.shortcuts import render, redirect

from AppClub.models import Inscripcion, Profesor, Copetencias, Profile


from AppClub.forms import AlumnoFormulario, ProfesorFormulario, CompetenciasFormulario, UserUpdateForm, UserProfileForm

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm,  PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

def inicio(request):
    forms = Inscripcion.objects.all()
    print(forms)
    return render(request, "AppClub\index.html")



def correct_edit(request):
    return render(request, "AppClub\devolucion\edit.html")

def dragones(request):
    return render(request, "AppClub\dragones.html")

# tablas (para mostrar los datos)

def tabla(request):
    forms= Inscripcion.objects.all()
    return render(request, "AppClub\Forms.html", {"forms":forms} )

def tablaProfes(request):
    formsProf= Profesor.objects.all()
    return render(request, "AppClub\FormsP.html", {"formsProf":formsProf} )

def tablaCompetencia(request):
    formsComp= Copetencias.objects.all()
    return render(request, "AppClub\FormsC.html", {"formsComp":formsComp} )

# formulario detallado 

def dealle_solicAlumno(request, id):
    alumno_form=Inscripcion.objects.get(id=id)
    return render(request, "AppClub\devolucion\detalle.html",{"alumno_form":alumno_form})

def detalle_solicProfe(request, id):
    profe_form=Profesor.objects.get(id=id)
    return render(request, "AppClub\devolucion\detalleP.html", {"profe_form":profe_form})

def detalle_soliComp(request, id):
    competencia_form=Copetencias.objects.get(id=id)
    return render(request, "AppClub\devolucion\detalleC.html",{"competencia_form":competencia_form})

# eliminacion de solicitudes (para eliminar datos):


def eliminar_solicAlumno(request, id):
    alumno=Inscripcion.objects.get(id=id)
    alumno.delete()
    return render(request, "AppClub\devolucion\delete.html")

def eliminar_solicProfe(request, id):
    profe=Profesor.objects.get(id=id)
    profe.delete()
    return render(request, "AppClub\devolucion\delete.html")

def eliminar_soliComp(request, id):
    competencia=Copetencias.objects.get(id=id)
    competencia.delete()
    return render(request, "AppClub\devolucion\delete.html")

# edit de solicitudes (para editar los datos)

def edit_solicAlumno(request, id):
    alumno=Inscripcion.objects.get(id=id)
    if request.method == "POST":
        alumno_form = AlumnoFormulario(request.POST)
        if alumno_form.is_valid():
            info_limpia = alumno_form.cleaned_data
            alumno.nombre = info_limpia["nombre"]
            alumno.apellido = info_limpia["apellido"]
            alumno.deporte = info_limpia["deporte"]
            alumno.save()
        return redirect("correct_edit")
    else:
        alumno_form = AlumnoFormulario(initial={"nombre":alumno.nombre, "apellido": alumno.apellido, "deporte": alumno.deporte})
    return render(request, "AppClub/forms/alumno_formedit.html", {"form":alumno_form})

def edit_solicProfe(request, id):
    profe=Profesor.objects.get(id=id)
    if request.method == "POST":
        profe_form = ProfesorFormulario(request.POST)
        if profe_form.is_valid():
            info_limpia = profe_form.cleaned_data
            profe.nombre = info_limpia["nombre"]
            profe.apellido = info_limpia["apellido"]
            profe.email = info_limpia["email"]
            profe.profesion = info_limpia["profesion"]
            profe.save()
        return redirect("correct_edit")
    else:
        profe_form = ProfesorFormulario(initial={"nombre":profe.nombre, "apellido": profe.apellido, "email": profe.email, "profesion": profe.profesion})
    return render(request, "AppClub/forms/profe_formedit.html", {"form":profe_form})

def edit_soliComp(request, id):
    comp=Copetencias.objects.get(id=id)
    if request.method == "POST":
        comp_form = CompetenciasFormulario(request.POST)
        if comp_form.is_valid():
            info_limpia = comp_form.cleaned_data
            comp.nombre = info_limpia["nombre"]
            comp.deporte = info_limpia["deporte"]
            comp.fecha = info_limpia["fecha"]
            comp.save()
        return redirect("correct_edit")
    else:
        comp_form = CompetenciasFormulario(initial={"nombre":comp.nombre, "deporte": comp.deporte, "fecha": comp.fecha})
    return render(request, "AppClub/forms/comp_formedit.html", {"form":comp_form})

# formularios (para crear datos)
@login_required(login_url="login_view")
def alumno_form(request):
    if request.method == "POST":
        alumno_form = AlumnoFormulario(request.POST)
        if alumno_form.is_valid():
            alumno_form.save()
            return redirect("inicio")
    else:
        alumno_form = AlumnoFormulario()
        return render(request, "AppClub/forms/alumno-formulario.html", {"form":alumno_form})

@login_required(login_url="login_view")
def profesor_form(request):
    if request.method == "POST":
        profesor_form = ProfesorFormulario(request.POST)
        if profesor_form.is_valid():
            profesor_form.save()
            return redirect("inicio")
    else:
        profesor_form = ProfesorFormulario()
        return render(request, "AppClub/forms/profesor-formulario.html", {"form":profesor_form})

@login_required(login_url="login_view")
def competencias_form(request):
    if request.method == "POST":
        competencias_form = CompetenciasFormulario(request.POST)
        if competencias_form.is_valid():
            competencias_form.save()
            return redirect("inicio")
    else:
            competencias_form = CompetenciasFormulario()
            return render(request, "AppClub/forms/competencias-formulario.html", {"form":competencias_form})

#log in, registrer, logout  

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
    else: 
        return render(request, "AppClub/forms/log_in.html")

def registrer_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = UserCreationForm()
    return render(request, "AppClub/forms/registrer.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('inicio')

# mostrar y editar prefil

def show_user(request):
    return render(request,"AppClub/profile/show_user.html")

def edit_user(request):
    
    usuario = request.user
    
    profile, _ = Profile.objects.get_or_create(user=usuario)
    
    if request.method == "POST":
        
        user_form=UserUpdateForm(request.POST, instance=usuario)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('show_user')
    
    else:
        user_form = UserUpdateForm(instance=usuario)
        profile_form = UserProfileForm()
    return render(request,"AppClub/profile/edit_user.html", {"user_form": user_form, "profile_form": profile_form})

def edit_password(request):
    usuario = request.user
    if request.method == "POST":
        password_form=PasswordChangeForm(usuario, request.POST)
        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request,usuario)
            return redirect('inicio')
    else:
        password_form=PasswordChangeForm(usuario)
    return render(request,"AppClub/profile/edit_password.html", {"password_form": password_form})


