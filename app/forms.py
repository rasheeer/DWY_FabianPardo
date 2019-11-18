from django import forms
from .models import Cliente, Servicio

class ClienteForm(forms.ModelForm):
    class Meta:
        model= Cliente
        fields= ['rut','nombre', 'apellido', 'edad', 'email', 'region']

class ServicioForm(forms.ModelForm):
    class Meta:
        model= Servicio
        fields= ['id_cliente']

