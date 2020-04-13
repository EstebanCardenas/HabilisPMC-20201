from django import forms
from .models import *

class PedidoForm(forms.ModelForm):
    direccion = forms.CharField(label="Dirección", widget=forms.TextInput(
        attrs={
            "placeholder":"Introduzca su dirección"
        }
    ))
    obj = Medicamento.objects.get(1).precio
    class Meta:
        model = Pedido
        fields = [
            'direccion'
        ]
