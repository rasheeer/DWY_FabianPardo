from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.CharField(max_length=50)
    region = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    id_cliente = models.ForeignKey(Cliente, null=True, on_delete=models.CASCADE)
    tipo_servicio = (
        ('Embargo', 'Embargo'),
        ('Deuda Educacional', 'Deuda Educacional(CAE)'),
        ('Dicom', 'Dicom'),
    )

    def __str__(self):
        return self.tipo_servicio

