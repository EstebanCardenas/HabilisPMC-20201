from django.shortcuts import render,redirect
#From Logic
from .logic.logic_productos import get_all_products,get_Product,get_precio_medicamento
# Create your views here.
from django.views import View
from medicamentos.forms import PedidoForm,MedicamentoPedidoForm
from .models import Medicamento


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
    template_name = 'Productos/slectProducto.html'
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


def get_productos(request):
    productos = list(get_all_products())
    context = {
        'productos': productos
    }
    return render(request, 'Productos/slectProducto.html', context)

def update_pedido(request,id):
    pedido= Medicamento.objects.get(pk=id)
    form = PedidoForm(request.POST or None, instance=pedido)
    if form.is_valid():
          form.save()
    return render(request, 'pedido_form.html',{'form':form, 'pedido': pedido})

def get_precio(request,nombre):
    medicamento=get_precio_medicamento(nombre)

