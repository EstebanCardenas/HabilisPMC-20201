from django import forms
from .logic.logicMedico import *
from .models import *

class FormularioOrdenMedica(forms.ModelForm):
    especialidad = forms.CharField(label="Especialidad", initial="HOLA")
    class Meta:
        model = Medico
        fields = [
            'especialidad'
        ]
