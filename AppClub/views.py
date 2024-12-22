from django.shortcuts import render

from AppClub.models import Inscripcion

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

def tabla(request):
    forms= Inscripcion.objects.all()
    return render(request, "AppClub\Forms.html", {"forms":forms} )