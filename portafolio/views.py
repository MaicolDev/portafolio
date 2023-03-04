from django.shortcuts import render,redirect
from .models import Proyecto
from .forms import ContactoForm

# Create your views here.


def home(request):

    proyectos =Proyecto.objects.all()
    return render (request,"home.html",{'proyectos': proyectos})

def contactar(request):

    if request.method == "GET":
        contacto = ContactoForm()
        return render (request,"contacto.html",{'contacto': contacto})

    else:
        contacto = ContactoForm()
        form = ContactoForm(request.POST)
        nuevo_contacto = form.save(commit=False)
        nuevo_contacto.save()
        return render (request,"contacto.html",{'contacto': contacto,"mensaje":"el mensaje fue enviado"})

    