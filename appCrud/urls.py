"""appCrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    # path('saludo', include('app.urls')),
    # path('addCarrera', include('app.urls')),
    # path('agregarCarrera', include('app.urls')),

    # path('editar_carrera/<int:carrera_id>', include('app.urls')),
    # path('listar_carreras_full', include('app.urls')),
    # path('borrar_carrera/<int:carrera_id>', include('app.urls')),
    # path('editar/<int:rut>', include('app.urls')),
    path('listar', include('app.urls')),
    path('registrocliente', include('app.urls')),
    path('abogados', include('app.urls')),
    path('index', include('app.urls')),
]
