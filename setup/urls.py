"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from rest_framework import routers
from api_telemetria.api import viewsets

route = routers.DefaultRouter()
route.register(r'marca', viewsets.MarcaViewset, basename="Marca")
route.register(r'modelo', viewsets.ModeloViewset, basename="Modelo")
route.register(r'veiculo', viewsets.VeiculoViewset, basename="Veículo")
route.register(r'unidademedida', viewsets.UnidadeMedidaViewset, basename="Unidade de medida")
route.register(r'medicao', viewsets.MedicaoViewset, basename="Medição")
route.register(r'medicaoveiculo', viewsets.MedicaoVeiculoViewset, basename="Medição do Veículo")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
