from django.shortcuts import render,redirect
from django.views import View
from usuarios.formsMedico import FormularioOrdenMedica
from habilis.auth0backend import getRole, getUserId
from django.contrib.auth.decorators import login_required
from django.contrib import messages

class FormularioOrdenView(View):
    template_name = 'medico2.html'
    def get(self, request, *args, **kwargs):
        form = FormularioOrdenMedica()
        context = {'form':form}
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        form = FormularioOrdenMedica(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Orden creada con éxito!')  
            form = FormularioOrdenMedica()
        context = {"form":form}
        return render(request, self.template_name, context)