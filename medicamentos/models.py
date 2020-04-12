from django.db import models

# Create your models here.

class Pedido(models.Model):
    #Atributos
    fecha = models.DateField(auto_now_add=True)
    direccion = models.CharField(max_length=100)
    precioTotal = models.FloatField()
    #Relaciones