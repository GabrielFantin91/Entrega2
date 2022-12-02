from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppCoder.forms import *
from django.template import Template, Context, loader

# Create your views here.



def area (request):
    return render (request, "AppCoder/Area.html")

def inicio (request):
    return render (request, "AppCoder/inicio.html")



def encargados (request):
        if request.method=="POST":
            form=encargadoForm(request.POST)
            if form.is_valid():
                informacion=form.cleaned_data
                nombre1=informacion["nombre"]
                apellido1=informacion["apellido"]
                email1=informacion["email"]
                profesion1=informacion["profesion"]
                encaregado1= encargado(nombre=nombre1,apellido=apellido1,email=email1,profesion=profesion1)
                encaregado1.save()
                return render (request, "AppCoder/inicio.html",{"mensaje":"Creo el encargado con exito"})
        else:
            formulario=encargadoForm()


        return render (request, "AppCoder/encargado.html", {"form":formulario})




def trabajadores (request):
    return render (request, "AppCoder/trabajadores.html")




def area_formulario (request):
    if request.method=="POST":
        form=areaForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre1=informacion["nombre"]
            numero1=informacion["numero"]
            area1= Area(nombre=nombre1,numero=numero1)
            area1.save()
            return render (request, "AppCoder/inicio.html",{"mensaje":"Creo el area con exito"})
    else:
        formulario=areaForm()


    return render (request, "AppCoder/AreaFormulario.html", {"form":formulario})
    

def busqueda_area(request):
    return render (request, "AppCoder/busqueda_area.html")

def buscar(request):
    if request.GET["area"]:
        numero1=request.GET["area"]
        areas=Area.objects.filter(numero=numero1)
        return render (request, "AppCoder/resultadoArea.html", {"area":areas})
    else:
        return render (request,"AppCoder/inicio.html",{"mensaje":"ingrese una numero de area"})

