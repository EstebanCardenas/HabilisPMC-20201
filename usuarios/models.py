from django.db import models

# Create your models here.

class Usuario(models.Model):
    #Atributos
    cedula = models.BigIntegerField()
    nombre = models.CharField(max_length=50)
    celular = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)

class Paciente(Usuario):
    #Atributos
    edad = models.IntegerField()
    #Relaciones
    eps = models.ForeignKey('eps.Eps', on_delete=models.CASCADE)
    #Funciones
    def __str__(self):
        '%s, %s' % (self.nombre, self.cedula.__str__())

class Medico(Usuario):
    #Atributos 
    regMedico= models.CharField(max_length=100)
    edad= models.SmallIntegerField()
    especialidad= models.CharField(max_length=120)
    #Relaciones:
    eps = models.ManyToManyField('eps.Eps')
    #Métodos
    def __str__(self):
        return '{}'.format(self.regMedico + "("+self.especialidad+")")
