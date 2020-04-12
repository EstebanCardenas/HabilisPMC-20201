from django import forms
from .models import *

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            'direccion'
        ]