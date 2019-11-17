from django import forms
from .models import Cliente, Servicio

class ClienteForm(forms.ModelForm):
    class Meta:
        model= Cliente
        fields= ['rut','nombre', 'apellido', 'edad', 'email', 'region']


