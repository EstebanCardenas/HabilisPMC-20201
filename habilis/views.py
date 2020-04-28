from django.http import HttpResponse
from django.shortcuts import render
from habilis.auth0backend import getRole 
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'base.html')

@login_required
def measurement_list(request):
    role = getRole(request)
    if role == "Médico":
        return render(request,'medico.html')

    elif role == "Paciente":
        return render(request,'paciente.html')
    else:
        return HttpResponse("Unauthorized User")