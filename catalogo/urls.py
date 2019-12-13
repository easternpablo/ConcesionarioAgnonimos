from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_vista, name="Login - Concesionario"),
    path("logout/", views.logout_vista, name="Logout - Concesionario"),
    path("marcas/", views.lista_marcas, name="Lista de marcas"),
    path("marcas/<marca_id>/", views.lista_coches, name="Lista de coches"), 
    path("cliente/registro/", views.registro_cliente, name="Registro cliente - Concesionario"),
    path("empleado/registro/", views.registro_empleado, name="Registro empleado - Concesionario"),
    path("nueva/marca/", views.agregar_marca, name="Registro marca - Concesionario"),
    path("nueva/compra/", views.agregar_compra, name="Nueva compra - Concesionario"),
    path("nuevo/coche/", views.agregar_coche, name="Registro coche - Concesionario"),
    path("listar/clientes/", views.listar_clientes, name="Listado clientes - Concesionario"),
    path("listar/proveedores/", views.listar_proveedores, name="Listado proveedores - Concesionario"),
    path("nuevo/proveedor/", views.agregar_proveedor, name="Registro proveedor - Concesionario"),
    path("listar/talleres/", views.listar_talleres, name="Listado talleres - Concesionario"),
    path("nuevo/taller/", views.agregar_taller, name="Registro taller - Concesionario"),
    path("compras/realizadas/", views.lista_compras, name="Listado compras - Concesionario"),
    path("reservar/coche/", views.agregar_reserva, name="Reservar coche - Concesionario"),
    path("listar/reservas/", views.listar_reservas, name="Listado reservas - Concesionario"),
    path("nueva/venta/", views.agregar_venta, name="Registro venta - Concesionario"),
    path("listar/ventas/", views.listar_ventas, name="Listado ventas - Concesionario"),
    path("", views.redireccion, name="Redirecion"),
]