from django.db import models

# Create your models here.

class Pedido(models.Model):
    #Atributos
    fecha = models.DateField(auto_now_add=True)
    direccion = models.CharField(max_length=100)
    precioTotal = models.FloatField()
    #Relaciones

class Medicamento(models.Model):
    #Atributos
    referencia: models.CharField(max_length=120)
    descripcion: models.CharField(max_length=200)
    indicaciones: models.CharField(max_length=250)
    precio: models.FloatField()
    #Relaciones

class MedicamentoPedido(models.Model):
    #Atributos
    cantidad: models.SmallIntegerField()
    precioTotal: models.FloatField()
    #Relaciones