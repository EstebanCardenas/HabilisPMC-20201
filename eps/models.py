from django.db import models

# Clase EPS
class Eps(models.Model):
    #Atributos
    nombre = models.CharField( max_length=40 , default='Sin nombre')

    #Métodos
    def __str__(self):
        return '{}'.format(self.nombre)

# Clase Cita
class Cita(models.Model):
    #Atributos
    tipo = models.CharField( max_length=40 , default='Sin nombre')
    fecha = models.DateTimeField()

    #Relaciones
    medico = models.ForeignKey('usuarios.Medico', on_delete=models.CASCADE , null = False , default=None)
    paciente = models.ForeignKey('usuarios.Paciente', on_delete=models.CASCADE , null = False , default=None)
    
    #Métodos
    def __str__(self):
        return '{}'.format(self.tipo + "("+self.fecha+")")

# Clase OrdenMedica
class OrdenMedica(models.Model):
    #Atributos
    numRegistro = models.BigIntegerField()
    emision = models.DateTimeField(auto_now_add=False)
    caducidad = models.DateTimeField(auto_now_add=False)

    #Relaciones
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE , null = False , default=None)
    medicamentos = models.ManyToManyField('medicamentos.Medicamento')
    
    #Métodos
    def __str__(self):
        return '{}'.format(self.cita + "("+self.emision + "-" + self.caducidad+")")