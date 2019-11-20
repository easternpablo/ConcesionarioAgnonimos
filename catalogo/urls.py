from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("catalogo/marcas/", views.lista_marcas, name="Lista de marcas"),
]