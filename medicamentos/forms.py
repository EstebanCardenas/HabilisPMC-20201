from django import forms
from .models import *
from .logic.logic_productos import *

class PedidoForm(forms.ModelForm):
    direccion = forms.CharField(label="Dirección", widget=forms.TextInput(
        attrs={
            "placeholder":"Introduzca su dirección"
        }
    ))
    class Meta:
        model = Pedido
        fields = [
            'direccion'
        ]


class MedicamentoPedidoForm(forms.ModelForm):
    cantidad = forms.IntegerField(label="Cantidad")
    medicamento = forms.ModelChoiceField(label="Medicamento", queryset=get_all_products())
    pedido = forms.ModelChoiceField(label="Pedido", queryset=get_pedidos())
    class Meta:
        model = MedicamentoPedido
        fields = [
            'medicamento',
            'cantidad',
            'pedido',
        ]