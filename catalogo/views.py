from django.shortcuts import render
from .models import Marca

# Vista donde se listan todas las marcas
def lista_marcas(request):
    marcas = Marca.objects.all()
    return render(request, "marcas.html", {"marcas": marcas})