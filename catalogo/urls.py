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
]