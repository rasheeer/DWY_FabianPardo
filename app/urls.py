from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.alumnos_list),
    # path('saludo', views.saludo_bienvenida),
    # path('agregarCarrera',views.inscripcion_carrera),
    # path('addCarrera', views.Carrera_Create.as_view(), name="carrera_crear"),
    # path('listar_carreras',views.listar_carreras),
    # path('borrar_carrera/<int:carrera_id>', views.borrar_carrera),
    # path('listar_carreras_full',views.listar_carreras_full),
    # path('editar/<int:rut>', views.editar_carrera),
    path('listar',views.listar_clientes),
    path('abogados',views.abogados),
    path('index',views.index),
    path('registrocliente',views.registro_cliente),
]
