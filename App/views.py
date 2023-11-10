from django.shortcuts import render

from App.models import *

# Create your views here.
def home(request):
    return render(request, "index.html")

def pinturas(request):
    pinturas = Pintura.objects.all()
    return render(request, "pages/pinturas.html", {"pinturas" : pinturas})

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, "pages/cursos.html", {"cursos" : cursos})

def contacto(request):
    return render(request, "pages/contacto.html")


