import django.forms as forms
from .models import *

class FormRegistroCliente(forms.ModelForm):
    nombre_usuario = forms.CharField(max_length= 20)
    class Meta:
        model = Cliente
        fields = ['dni', 'nombre', 'apellidos', 'telefono', 'nacimiento', 'direccion', 'email']

class FormLogin(forms.Form):
	nombre = forms.CharField(max_length = 20)
	password = forms.CharField(max_length = 20, widget=forms.PasswordInput)