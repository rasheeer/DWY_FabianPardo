from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('borrar_cliente/<int:rut>', views.borrar_cliente),
    path('crud',views.todo_junto),
    path('editar/<int:id_cliente>', views.editar_cliente),
    path('listar',views.listar_clientes),
    path('abogados',views.abogados),
    path('index',views.index),
    path('registrocliente',views.registro_cliente),
]
