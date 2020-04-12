from django import forms
from .models import *

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
