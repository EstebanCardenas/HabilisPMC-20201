from django.shortcuts import render,redirect
#From Logic
# Create your views here.
from django.views import View
from medicamentos.forms import PedidoForm,MedicamentoPedidoForm

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

class CreateMedicamentoProducto(View):
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