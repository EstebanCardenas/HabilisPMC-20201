from django import forms
from .logic.logicMedico import *
from .models import *
from django.http import HttpRequest
from habilis.views import getPutoId
from .logic.logicMedico import *
from django.core.exceptions import ObjectDoesNotExist
import datetime




class FormularioOrdenMedica(forms.Form):

    userIdMedico = getPutoId
    try: 
        Medico.objects.get(user_id=userIdMedico)
    except ObjectDoesNotExist:
        userIdMedico = "auth0|5ea761721cc1ac0c146c32e2"
    m = Medico.objects.get(user_id=userIdMedico)
    

    nombreMedico = forms.CharField(label="Nombre Médico", initial=m.nombre, disabled = True)
    especialidad = forms.CharField(label="Especialidad", initial=m.especialidad, disabled = True)
    edad = forms.CharField(label="Edad", initial=m.edad, disabled = True)
    registroMedico = forms.CharField(label="Número de registro médico", initial=m.regMedico, disabled = True)
    fecha = forms.DateField(initial=datetime.date.today, disabled = True)
    nombrePaciente = forms.ModelChoiceField(label="Nombre paciente", queryset=getPacientes())
    cedulaPaciente = forms.CharField(label="Cédula del paciente")
    uso = forms.CharField(label="Uso")
    indicaciones = forms.CharField(label="Indicaciones")
    cantidad = forms.IntegerField(label="Cantidad", initial=1)
    duracion = forms.CharField(label="Duración")
    


    class Meta:
        model = OrdenMedicaMedico
        fields = [
            'nombreMedico',
            'especialidad',
            'edad',
            'registroMedico',
            'fecha',
            'nombrePaciente',
            'cedulaPaciente',
            'uso',
            'indicaciones',
            'cantidad',
            'duracion',
        ]
