from django.shortcuts import render
from AppVeterinaria.forms import *
from AppVeterinaria.models import *
# Create your views here.

def inicio(request): 
    return render(request, "AppVeterinaria/inicio.html")
    
def ver_profesionales(request):

    profesionales = Profesional.objects.all()

    return render(request, "AppVeterinaria/verProfesionales.html", {"profesionales": profesionales})

def agregar_profesionales(request): 

    if request.method == "POST":
        
        miFormulario =  ProfesionalFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesional = Profesional(nombre_completo=informacion["nombre_completo"], fecha_nacimiento=informacion["fecha_nacimiento"], email=informacion["email"], dni=informacion["dni"], especialidad=informacion["especialidad"], esta_recibido=informacion["esta_recibido"], esta_activo=informacion["esta_activo"] )
            profesional.save()
            return render(request, "AppVeterinaria/verProfesionales.html")
    else:
        miFormulario = ProfesionalFormulario()
        
    return render(request, "AppVeterinaria/profesionalFormulario.html", {"miFormulario": miFormulario})

def buscar_profesionales(request):

    return render(request, "AppVeterinaria/buscarProfesional.html")

def resultado_profesionales(request):

    profesional_buscado = request.GET["nombre_completo"]
    resultados_profesionales = Profesional.objects.filter(nombre_completo__icontains=profesional_buscado)

    return render(request, "AppVeterinaria/resultadoProfesionales.html", {"nombre_buscado":profesional_buscado, "profesionales": resultados_profesionales})


def ver_visitas(request):

    visitas = Visita.objects.all()

    return render(request, "AppVeterinaria/verVisitas.html", {"visitas": visitas})

def agregar_visitas(request): 

    if request.method == "POST":
        
        miFormulario =  VisitaFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            visita = Visita(
               fecha_visita=informacion["fecha_visita"],
               nombre_paciente=informacion["nombre_paciente"],
               nombre_profesional=informacion["nombre_profesional"],
               diagnostico=informacion["diagnostico"],
               medicacion=informacion["medicacion"],
               proximo_control=informacion["proximo_control"] 
            )
            visita.save()
            return render(request, "AppVeterinaria/verVisitas.html")
    else:
        miFormulario = VisitaFormulario()
        
    return render(request, "AppVeterinaria/visitaFormulario.html", {"miFormulario": miFormulario})

def buscar_visitas(request):

    return render(request, "AppVeterinaria/buscarVisita.html")

def resultado_visitas(request):

    paciente_buscado = request.GET["nombre_paciente"]
    resultados_visitas = Visita.objects.filter(nombre_paciente__icontains=paciente_buscado)

    return render(request, "AppVeterinaria/resultadoVisitas.html", {"nombre_buscado":paciente_buscado, "visitas": resultados_visitas})


def ver_pacientes(request):

    pacientes = Paciente.objects.all()

    return render(request, "AppVeterinaria/verPacientes.html", {"pacientes": pacientes})

def agregar_pacientes(request): 

    if request.method == "POST":
        
        miFormulario =  PacienteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            paciente = Paciente(
                especie=informacion["especie"],
                raza=informacion["raza"],
                nombre=informacion["nombre"],
                fecha_nacimiento=informacion["fecha_nacimiento"],
                sexo=informacion["sexo"],
                esta_castrado=informacion["esta_castrado"],
                direccion=informacion["direccion"],
                dni_tutor=informacion["dni_tutor"]
            )
            paciente.save()
            return render(request, "AppVeterinaria/verPacientes.html")
    else:
        miFormulario = PacienteFormulario()
        
    return render(request, "AppVeterinaria/pacienteFormulario.html", {"miFormulario": miFormulario})

def buscar_pacientes(request):

    return render(request, "AppVeterinaria/buscarPaciente.html")

def resultado_pacientes(request):

    paciente_buscado = request.GET["nombre"]
    resultados_pacientes = Paciente.objects.filter(nombre__icontains=paciente_buscado)

    return render(request, "AppVeterinaria/resultadoPacientes.html", {"nombre_buscado":paciente_buscado, "pacientes": resultados_pacientes})

