from django.db import models

# Create your models here.

class Pedido(models.Model):
    #Atributos
    fecha = models.DateField(auto_now_add=True)
    direccion = models.CharField(max_length=100)
    precioTotal = models.FloatField()
    #Relaciones
    paciente = models.ForeignKey('usuarios.Paciente', on_delete=models.CASCADE)
    #Funciones
    def __str__(self):
        '%s, %s, %s, $s' % (self.fecha.__str__(), self.direccion, self.precioTotal.__str__(), self.paciente.nombre)

class Medicamento(models.Model):
    #Atributos
    referencia = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=200)
    indicaciones = models.CharField(max_length=250)
    precio = models.FloatField()
    
    #Métodos
    def __str__(self):
        return '{}'.format(self.referencia)

class MedicamentoPedido(models.Model):
    #Atributos
    cantidad= models.SmallIntegerField()
    precioTotal= models.FloatField()
    #Relaciones
    medicamento = models.OneToOneField(Medicamento, on_delete = models.CASCADE, primary_key = True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE , null = False , default=None)
    #Métodos
    def __str__(self):
        return '{}'.format(self.medicamento + " Cantidad: " + self.cantidad)

