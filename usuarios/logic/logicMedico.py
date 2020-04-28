from ..models import *

def getMedico():
    return Medico.objects.get(regMedico="321")