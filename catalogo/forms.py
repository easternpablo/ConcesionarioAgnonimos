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

class FormLogin(forms.Form):
	nombre = forms.CharField(max_length = 20)
	password = forms.CharField(max_length = 20, widget=forms.PasswordInput)