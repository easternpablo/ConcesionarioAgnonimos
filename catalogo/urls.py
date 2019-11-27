from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_vista, name="Login - Concesionario"),
    path("logout/", views.logout_vista, name="Logout - Concesionario"),
    path("marcas/", views.lista_marcas, name="Lista de marcas"),
    path("marcas/<marca_id>/", views.lista_coches, name="Lista de coches"), 
    path("cliente/registro/", views.registro_cliente, name="Registro cliente - Concesionario"),
]