from ..models import *
from django.core.exceptions import ObjectDoesNotExist

def getPacientes():
    pacientes = Paciente.objects.all()
    return pacientes