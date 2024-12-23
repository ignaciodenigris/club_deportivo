from django.shortcuts import render

from AppClub.models import Inscripcion, Profesor, Copetencias

from django.http import HttpResponse

def inicio(request):
    forms = Inscripcion.objects.all()
    print(forms)
    return render(request, "AppClub\index.html")

def inscripcion(request):
    if request.method == "POST":
        inscripcion = Inscripcion(nombre=request.POST["nombre"],apellido=request.POST["apellido"],deporte=request.POST["deporte"])
        inscripcion.save()
        return render(request, "AppClub\inscripciones.html")
    else:
        return render(request, "AppClub\inscripciones.html")


def nav (request):
    query = request.GET.get("q")
    if query:
        nav = Inscripcion.objects.filter(nombre__icontains = query)
    else:
        nav =  Inscripcion.objects.all()
    return render(request, "AppClub\Forms.html", {"nav":forms} )



def inscripcion(request):
    if request.method == "POST":
        inscripcion = Inscripcion(nombre=request.POST["nombre"],apellido=request.POST["apellido"],deporte=request.POST["deporte"])
        inscripcion.save()
        return render(request, "AppClub\inscripciones.html")
    else:
        return render(request, "AppClub\inscripciones.html")


def tabla(request):
    forms= Inscripcion.objects.all()
    return render(request, "AppClub\Forms.html", {"forms":forms} )







def SolicitudProfesor (request):
    if request.method == "POST":
        solicitud = Profesor(nombre=request.POST["nombre"],apellido=request.POST["apellido"],email=request.POST["email"], profesion=request.POST["profesion"])
        solicitud.save()
        return render(request, "AppClub\Profesores.html")
    else:
        return render(request, "AppClub\Profesores.html")

def tablaProfes(request):
    formsProf= Profesor.objects.all()
    return render(request, "AppClub\FormsP.html", {"formsProf":formsProf} )

def SolicitudCompetencia (request):
    if request.method == "POST":
        solicitud = Copetencias(nombre=request.POST["nombre"],deporte=request.POST["deporte"], fechaDeCopetencia=request.POST["fecha"])
        solicitud.save()
        return render(request, "AppClub\Copetencias.html")
    else:
        return render(request, "AppClub\Copetencias.html")

def tablaCompetencia(request):
    formsComp= Copetencias.objects.all()
    return render(request, "AppClub\FormsC.html", {"formsComp":formsComp} )