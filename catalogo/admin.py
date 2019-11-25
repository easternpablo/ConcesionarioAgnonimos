from django.contrib import admin
from .models import Marca, Coche, Taller, Cliente, Empleado, Proveedor, Compra, Venta

admin.site.register(Marca)
admin.site.register(Coche)
admin.site.register(Taller)
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Proveedor)
admin.site.register(Compra)
admin.site.register(Venta)