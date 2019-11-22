from django.shortcuts import render
from .models import Marca, Coche

# Vista donde se listan todas las marcas
def lista_marcas(request):
    marcas = Marca.objects.all()
    return render(request, "marcas.html", {"marcas": marcas})

def lista_coches(request,marca_id):
    coches = Coche.objects.filter(marca_id__nombre = marca_id)
    return render(request,"coche.html",{"coches":coches})

