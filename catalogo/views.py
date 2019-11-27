from django.shortcuts import render, redirect
from .models import Marca, Coche
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# Vista donde se listan todas las marcas
@login_required(login_url="/concesionario/login")
def lista_marcas(request):
    marcas = Marca.objects.all()
    return render(request, "marcas.html", {"marcas": marcas})

@login_required(login_url="/concesionario/login")
def lista_coches(request,marca_id):
    coches = Coche.objects.filter(marca_id__nombre = marca_id)
    return render(request,"coche.html",{"coches":coches})

@login_required(login_url="/concesionario/login")
def agregar_marca(request):
    if request.POST:
        form = FormRegistroMarcas(request.POST, request.FILES)
        if form.is_valid():
            nueva_marca = form.save()
            return redirect("/concesionario/marcas")
        else:
            return render(request, "registroMarca.html", {'form':form})
    else:
        form = FormRegistroMarcas()
        return render(request, "registroMarca.html", {'form':form})

@login_required(login_url="/concesionario/login")
def agregar_coche(request):
    if request.POST:
        form = FormRegistroCoches(request.POST, request.FILES)
        if form.is_valid():
            nuevo_coche = form.save()
            return redirect("/concesionario/nueva/compra")
        else:
            return render(request, "formularioCoche.html", {'form':form})
    else:
        form = FormRegistroCoches()
        return render(request, "formularioCoche.html", {'form':form})

@login_required(login_url="/concesionario/login")
def agregar_compra(request):
    if request.POST:
        form = FormCompraCoche(request.POST, request.FILES)
        if form.is_valid():
            compra = form.save()
            return redirect("/concesionario/marcas")
        else:
            return render(request, "registroCoche.html", {'form':form})
    else:
        form = FormCompraCoche()
        return render(request, "registroCoche.html", {'form':form})

def registro_cliente(request):
    if request.user.username:
        return redirect("/concesionario/marcas")   #donde nos va a llevar cuando esté logueado
    if request.POST:
        formulario = FormRegistroCliente(request.POST)
        nuevo_nombre = request.POST['nombre_usuario']       #el nombre que hemos puesto en forms
        usuario = User.objects.filter(username=nuevo_nombre)
        if len(usuario)>0:
            return render(request,'registroCliente.html',{'form':formulario, 'mensaje':"Nombre de usuario existente"})
        usuario = User.objects.create_user(nuevo_nombre,"cliente@gmail.com","cliente")
        usuario.save()
        nuevo_cliente = formulario.save()
        nuevo_cliente.usuario = usuario
        nuevo_cliente.save()
        return redirect("/concesionario/login")
    else:
        formulario = FormRegistroCliente()
    return render(request, "registroCliente.html", {'form':formulario})

def registro_empleado(request):
    if request.user.username:
        return redirect("/concesionario/marcas")   #donde nos va a llevar cuando esté logueado
    if request.POST:
        formulario = FormRegistroEmpleados(request.POST)
        nuevo_nombre = request.POST['nombre_usuario']       #el nombre que hemos puesto en forms
        usuario = User.objects.filter(username=nuevo_nombre)
        if len(usuario)>0:
            return render(request,'registroEmpleados.html',{'form':formulario, 'mensaje':"Nombre de usuario existente"})
        usuario = User.objects.create_user(nuevo_nombre,"empleado@gmail.com","empleado")
        usuario.save()
        nuevo_empleado = formulario.save()
        nuevo_empleado.usuario = usuario
        nuevo_empleado.save()
        return redirect("/concesionario/login")
    else:
        formulario = FormRegistroEmpleados()
    return render(request, "registroEmpleados.html", {'form':formulario})

def login_vista(request):
    if request.user.username:
        return redirect("/concesionario/marcas")
    if request.POST:
        formulario = FormLogin(request.POST)
        user = authenticate(username=request.POST['nombre'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            if 'next' in request.GET:
                return redirect(request.GET['next'])
            else:
                return redirect("/concesionario/marcas")
    else:
        formulario = FormLogin()
    return render(request, "login.html", {'form':formulario})

def logout_vista(request):
    logout(request)
    return redirect("/concesionario/login")