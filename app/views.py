from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# -----------  para nuestos modelos --------------------
from .models import Cliente
#from mantenedor.app.forms import CarreraForm
from .forms import ClienteForm


def abogados(request):
    return render(request, 'app/abogados.html', {})

def index(request):
    return render(request, 'app/index.html', {})



# ====== FUNCIONES ======
# REGISTRO DE CLIENTE
def registro_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/registrocliente')
    else:
        form = ClienteForm()
        return render(request, 'app/registrocliente.html',
                      {'form': form})

def listar_clientes(request):
    # creamos una colección la cual carga TODOS los registos
    clientes = Cliente.objects.all()
    # renderizamos la colección en el template
    return render(request,
        "app/listar.html", {'clientes': clientes})
    

def listar_carreras(request):
    # creamos una colección la cual carga TODOS los registos
    carreras = Carrera.objects.all()
    # renderizamos la colección en el template
    return render(request,
        "app/listar_carreras.html", {'carreras': carreras})


def editar_cliente(request, id_cliente):
    instancia= Servicio.objects.get(id=id_cliente)
    form=  ServicioForm(instance=instancia)
    if request.method=="POST":
        form= ServicioForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia= form.save(commit=False)
            instancia.save()
    return render(request, "app/editar.html",{'form':form})

def borrar_cliente(request, rut):
    instacia= Carrera.objects.get(id=rut)
    instacia.delete()
    return redirect('/')

def todo_junto(request):
    clientes = Cliente.objects.all()
    return render(request,
        "app/crud.html", {'clientes': clientes})

