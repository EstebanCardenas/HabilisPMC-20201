from usuarios.models import Paciente
from medicamentos.models import Medicamento
from eps.models import Cita
from django.core.exceptions import ObjectDoesNotExist

def getPacientes():
    pacientes = Paciente.objects.all()
    return pacientes

def getMedicamentos():
    medicamentos = Medicamento.objects.all()
    return medicamentos

def getCitas():
    citas = Cita.objects.all()
    return citas