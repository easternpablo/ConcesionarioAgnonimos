from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


@login_required(login_url="/concesionario/login")
def lista_marcas(request):
    marcas = Marca.objects.all()
    return render(request, "marcas.html", {"marcas": marcas})

@login_required(login_url="/concesionario/login")
def lista_coches(request,marca_id):
    coches = Coche.objects.filter(marca_id__nombre = marca_id, vendido = False)
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
def editar_marca(request,marca_id):
    marca = Marca.objects.get(nombre=marca_id)
    formEdit = FormEditarMarcas(instance = marca)
    if request.POST:
        formEdit = FormEditarMarcas(request.POST, instance = marca)
        if formEdit.is_valid:
            marca = formEdit.save(commit=False)
            marca.save()
            return redirect("/concesionario/marcas")
    return render(request, "editarMarca.html", {'form':formEdit})

@login_required(login_url="/concesionario/login")
def editar_coche(request,coche_id):
    coche = Coche.objects.get(coche_id=coche_id)
    formEdit = FormEditarCoches(instance = coche)
    if request.POST:
        formEdit = FormEditarCoches(request.POST, instance = coche)
        if formEdit.is_valid:
            coche = formEdit.save(commit=False)
            coche.save()
            return redirect("/concesionario/marcas")
    return render(request, "editarCoche.html", {'form':formEdit})

@login_required(login_url="/concesionario/login")
def eliminar_marca(request,marca_id):
    marca = Marca.objects.get(nombre=marca_id)
    marca.delete()
    return redirect("/concesionario/marcas")

@login_required(login_url="/concesionario/login")
def eliminar_coche(request,coche_id):
    coche = Coche.objects.get(coche_id=coche_id)
    coche.delete()
    return redirect("/concesionario/marcas")

@login_required(login_url="/concesionario/login")
def agregar_proveedor(request):
    if request.POST:
        form = FormRegistroProveedores(request.POST, request.FILES)
        if form.is_valid():
            nuevo_proveedor = form.save()
            return redirect("/concesionario/listar/proveedores")
        else:
            return render(request, "registroProveedor.html", {'form':form})
    else:
        form = FormRegistroProveedores()
        return render(request, "registroProveedor.html", {'form':form})

@login_required(login_url="/concesionario/login")
def agregar_taller(request):
    if request.POST:
        form = FormRegistroTalleres(request.POST, request.FILES)
        if form.is_valid():
            nuevo_taller = form.save()
            return redirect("/concesionario/listar/talleres")
        else:
            return render(request, "registroTaller.html", {'form':form})
    else:
        form = FormRegistroTalleres()
        return render(request, "registroTaller.html", {'form':form})

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

@login_required(login_url="/concesionario/login")
def agregar_venta(request):
    if request.POST:
        form = FormRegistroVenta(request.POST, request.FILES)
        if form.is_valid():
            venta = form.save()
            coche = venta.coche_id
            coche.vendido = True
            coche.save(update_fields=["vendido"])
            return redirect("/concesionario/nueva/venta")
        else:
            return render(request, "registroVenta.html", {'form':form})
    else:
        form = FormRegistroVenta()
        return render(request, "registroVenta.html", {'form':form})

@login_required(login_url="/concesionario/login")
def agregar_reserva(request):
    if request.POST:
        form = FormRegistroReserva(request.POST, request.FILES)
        if form.is_valid():
            reserva = form.save()
            return redirect("/concesionario/reservar/coche")
        else:
            return render(request, "reservarCoche.html", {'form':form})
    else:
        form = FormRegistroReserva()
        return render(request, "reservarCoche.html", {'form':form})

@login_required(login_url="/concesionario/login")
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "listar_clientes.html",{"clientes":clientes})

@login_required(login_url="/concesionario/login")
def listar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, "listar_reservas.html",{"reservas":reservas})

@login_required(login_url="/concesionario/login")
def listar_ventas(request):
    ventas = Venta.objects.all()
    return render(request, "listar_ventas.html",{"ventas":ventas})

@login_required(login_url="/concesionario/login")
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, "listar_proveedores.html",{"proveedores":proveedores})

@login_required(login_url="/concesionario/login")
def listar_talleres(request):
    talleres = Taller.objects.all()
    return render(request, "listar_talleres.html",{"talleres":talleres})

@login_required(login_url="/concesionario/login")
def lista_compras(request):
    compras = Compra.objects.all()
    return render(request,"compras_realizadas.html",{"compras":compras})

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

def redireccion(request):
    return redirect("/concesionario/login")