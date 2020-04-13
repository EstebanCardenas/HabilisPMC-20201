from ..models import Medicamento,MedicamentoPedido
from django.core.exceptions import ObjectDoesNotExist

def get_all_products():
    productos = Medicamento.objects.all()
    return productos

def get_Product(producto):
    try:
        Medicamento.objects.get(referencia=producto)
    except ObjectDoesNotExist:
        return 0
    med = Medicamento.objects.get(referencia=producto)
    return Medicamento.objects.get(referencia=producto)

def get_precio_medicamento(nombre):
    producto = Medicamento.objects.filter(referencia = nombre).precio
    return producto