from django.urls import path
from AppVeterinaria.views import *
urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('profesionales/', ver_profesionales, name="Profesionales"),
    path('agregarProfesional/', agregar_profesionales, name="Agregar_Profesionales"),
    path("buscarProfesional/", buscar_profesionales, name="Buscar_Profesionales"),
    path("resultadoProfesionales/", resultado_profesionales, name="Resultado_Profesionales"),

    path('visitas/', ver_visitas, name="Visitas"),
    path('agregarVisita/', agregar_visitas, name="Agregar_Visitas"),
    path("buscarVisita/", buscar_visitas, name="Buscar_Visitas"),
    path("resultadoVisitas/", resultado_visitas, name="Resultado_Visitas"),

    path('pacientes/', ver_pacientes, name="Pacientes"),
    path('agregarPaciente/', agregar_pacientes, name="Agregar_Pacientes"),
    path("buscarPaciente/", buscar_pacientes, name="Buscar_Pacientes"),
    path("resultadoPacientes/", resultado_pacientes, name="Resultado_Pacientes"),
]