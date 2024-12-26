from django.shortcuts import render, redirect

from AppClub.models import Inscripcion, Profesor, Copetencias


from AppClub.forms import AlumnoFormulario, ProfesorFormulario, CompetenciasFormulario


from django.http import HttpResponse

def inicio(request):
    forms = Inscripcion.objects.all()
    print(forms)
    return render(request, "AppClub\index.html")

def correct_edit(request):
    return render(request, "AppClub\devolucion\edit.html")

def nav (request):
    query = request.GET.get("q")
    if query:
        nav = Inscripcion.objects.filter(nombre__icontains = query)
    else:
        nav =  Inscripcion.objects.all()
    return render(request, "AppClub\Forms.html", {"nav":forms} )


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

def alumno_form(request):
    if request.method == "POST":
        alumno_form = AlumnoFormulario(request.POST)
        if alumno_form.is_valid():
            alumno_form.save()
            return redirect("inicio")
    else:
        alumno_form = AlumnoFormulario()
        return render(request, "AppClub/forms/alumno-formulario.html", {"form":alumno_form})

def profesor_form(request):
    if request.method == "POST":
        profesor_form = ProfesorFormulario(request.POST)
        if profesor_form.is_valid():
            profesor_form.save()
            return redirect("inicio")
    else:
        profesor_form = ProfesorFormulario()
        return render(request, "AppClub/forms/profesor-formulario.html", {"form":profesor_form})


def competencias_form(request):
    if request.method == "POST":
        competencias_form = CompetenciasFormulario(request.POST)
        if competencias_form.is_valid():
            competencias_form.save()
            return redirect("inicio")
    else:
            competencias_form = CompetenciasFormulario()
            return render(request, "AppClub/forms/competencias-formulario.html", {"form":competencias_form})


