from django.shortcuts import render,redirect
#From Logic
# Create your views here.
from django.views import View

from eps.models import OrdenMedica
from medicamentos.forms import *

class PedidoCreateView(View):
    template_name = 'pedidos/create.html'
    def get(self, request, *args, **kwargs):
        form = PedidoForm()
        context = {'form':form}
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            form = PedidoForm()
        context = {"form":form}
        return render(request, self.template_name, context)

class CreateMedicamentoProductoView(View):
    template_name = 'productos/slectProducto.html'
    def get(self, request, *args, **kwargs):
        form = MedicamentoPedidoForm()
        context = {'form':form}
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        form = MedicamentoPedidoForm(request.POST)
        if form.is_valid():
            form.save()
            form = MedicamentoPedidoForm()
        context = {"form":form}
        return render(request, self.template_name, context)

class ValidarOrdenMedicaView(View):
    template_name = 'orden_medica/validar_orden.html'
    def get(self, request, *args, **kwargs):
        form = OrdenMedicaForm()
        context = {
            'form':form
        }
        return render(request, self.template_name, context)
    def get_queryset(self, request):
        numReg = request.GET.get('q')
        orden = OrdenMedica.objects.filter(numRegistro=numReg)
        context = {'orden':orden}
        if orden != None:
            return render(request, 'orden_medica/orden_encontrada.html', context)