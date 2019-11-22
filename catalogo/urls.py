from django.urls import path
from . import views

urlpatterns = [
    path("catalogo/marcas/", views.lista_marcas, name="Lista de marcas"),
]