from django.shortcuts import render

from django.http import HttpResponse

def inicio(request):
    return render(request, "AppClub\index.html")