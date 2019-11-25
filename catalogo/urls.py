from django.urls import path
from . import views

urlpatterns = [
    path("catalogo/marcas/", views.lista_marcas, name="Lista de marcas"),
    path("catalogo/marcas/<marca_id>/", views.lista_coches, name="Lista de coches"),
]