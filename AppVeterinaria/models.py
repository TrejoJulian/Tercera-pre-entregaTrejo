from django.db import models

# Create your models here.
class Profesional (models.Model):
    nombre_completo = models.CharField(max_length=64)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    dni = models.CharField(max_length=9)
    especialidad = models.CharField(max_length=64)
    esta_recibido = models.BooleanField()
    esta_activo = models.BooleanField()

class Paciente (models.Model):
    especie = models.CharField(max_length=64)
    raza = models.CharField(max_length=64)
    nombre = models.CharField(max_length=64)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=20)
    esta_castrado = models.BooleanField()
    direccion = models.CharField(max_length=64)
    dni_tutor = models.CharField(max_length=9)

class Visita (models.Model):
    fecha_visita = models.DateField()
    nombre_paciente = models.CharField(max_length=64)
    nombre_profesional = models.CharField(max_length=64)
    diagnostico = models.CharField(max_length= 255)
    medicacion = models.CharField(max_length= 255, blank=True)
    proximo_control = models.DateField()