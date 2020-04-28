from django.db import models

# Create your models here.

class Usuario(models.Model):
    #Atributos
    cedula = models.BigIntegerField(null=True, blank=True)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    celular = models.CharField(max_length=50, null=True, blank=True)
    correo = models.CharField(max_length=50, null=True, blank=True)

class Paciente(Usuario):
    #Atributos
    edad = models.IntegerField(null=True, blank=True)
    #Relaciones
    eps = models.ForeignKey('eps.Eps', on_delete=models.CASCADE, null=True, blank=True)
    #Funciones
    def __str__(self):
        return '{}'.format(self.nombre + "("+self.cedula.__str__()+")")

class Medico(Usuario):
    #Atributos 
    nombreMedico = models.CharField(max_length=50, null=True, blank=True)
    apellidoMedico = models.CharField(max_length=50, null=True, blank=True)
    regMedico= models.CharField(max_length=100, null=True, blank=True)
    edad= models.SmallIntegerField(null=True, blank=True)
    especialidad= models.CharField(max_length=120, null=True, blank=True)
    #Relaciones:
    eps = models.ManyToManyField('eps.Eps', blank=True)
    #Métodos
    def __str__(self):
        return '{}'.format(self.regMedico + "("+self.especialidad+")")


class OrdenMedicaMedico(Usuario):
    #Atributos 
    fecha= models.DateField(auto_now_add=True, null=True, blank=True)
    uso= models.CharField(max_length=120, null=True, blank=True)
    indicaciones = models.CharField(max_length=120, null=True, blank=True)
    cantidad = models.SmallIntegerField(null=True, blank=True)
    duracion = models.CharField(max_length=120, null=True, blank=True)
    #Relaciones:
    medicoAsociaco = models.ForeignKey(Medico, on_delete=models.CASCADE, null=True, blank=True)
    pacienteAsociado = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True, blank=True)
    medicamentoAsociado = models.ForeignKey('medicamentos.Medicamento', on_delete=models.CASCADE, null=True, blank=True)
    #Métodos
    def __str__(self):
        return '{}'.format(self.regMedico + "("+self.especialidad+")")
