"""
URL configuration for sun_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from veterinarios import views
from veterinarios.views import agregar_veteri, ver_veteri, editar_veteri, eliminar_veteri, generar_reporte
from webapp.views import ver_veterinarios

router = routers.DefaultRouter()
router.register(r'veterinarios', views.vete_ViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ver_veterinarios, name='inicio'),
    path('agregar_veteri/', agregar_veteri),
    path('ver_veteri/<int:idVeterinario>', ver_veteri),
    path('editar_veteri/<int:idVeterinario>', editar_veteri),
    path('eliminar_veteri/<int:idVeterinario>', eliminar_veteri),
    path('generar_reporte/', generar_reporte),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
