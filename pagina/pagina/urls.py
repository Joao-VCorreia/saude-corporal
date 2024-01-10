from django.contrib import admin
from django.urls import path, include
from ingressar import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ingressar.urls',)),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastrar_paciente', views.cadastrar_paciente, name='cadastrar_paciente'),
    path('listar_pacientes/', views.listar_pacientes, name='listar_pacientes'),
    path('pesquisar_pacientes/', views.pesquisar_pacientes, name='pesquisar_pacientes'),
]
