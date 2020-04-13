from django import forms
from .models import *
from .logic.logic_productos import get_all_products,get_precio_medicamento

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
    medicamento = forms.ModelChoiceField(label="Medicamento",queryset=get_all_products())
    precioTotal= cantidad * get_precio_medicamento(medicamento)
    class Meta:
        model = MedicamentoPedido
        fields = [
            'medicamento',
            'cantidad',
        ]
