from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class ProfesionalFormulario (forms.Form):
    nombre_completo = forms.CharField()
    fecha_nacimiento = forms.DateField(widget=DateInput)
    email = forms.EmailField()
    dni = forms.CharField()
    especialidad = forms.CharField()
    esta_recibido = forms.BooleanField(initial=False, required=False)
    esta_activo = forms.BooleanField(initial=False, required=False)

class PacienteFormulario (forms.Form):
    especie = forms.CharField()
    raza = forms.CharField()
    nombre = forms.CharField()
    fecha_nacimiento = forms.DateField(widget=DateInput)
    sexo = forms.CharField()
    esta_castrado = forms.BooleanField(initial=False, required=False)
    direccion = forms.CharField()
    dni_tutor = forms.CharField()

class VisitaFormulario (forms.Form):
    fecha_visita = forms.DateField(widget=DateInput)
    nombre_paciente = forms.CharField()
    nombre_profesional = forms.CharField()
    diagnostico = forms.CharField()
    medicacion = forms.CharField()
    proximo_control = forms.DateField(widget=DateInput)