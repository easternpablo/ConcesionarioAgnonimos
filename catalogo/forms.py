import django.forms as forms
from .models import *

class FormRegistroCliente(forms.ModelForm):
    nombre_usuario = forms.CharField(max_length= 20)
    class Meta:
        model = Cliente
        fields = ['dni', 'nombre', 'apellidos', 'telefono', 'direccion', 'email']

class FormRegistroEmpleados(forms.ModelForm):
    nombre_usuario = forms.CharField(max_length= 20)
    class Meta:
        model = Empleado
        fields = ['dni', 'nombre', 'apellidos', 'telefono', 'direccion', 'email','puesto']

class FormRegistroMarcas(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre','imagen','taller_id']

class FormCompraCoche(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['coche_id','proveedor_id','empleado_id']

class FormRegistroCoches(forms.ModelForm):
    class Meta:
        model = Coche
        fields = ['marca_id','matricula','modelo','kilometros','color','motor','tipo','caballos','cilindradas','precio','vendido','imagen']

class FormLogin(forms.Form):
    nombre = forms.CharField(max_length = 20)
    password = forms.CharField(max_length = 20, widget=forms.PasswordInput)