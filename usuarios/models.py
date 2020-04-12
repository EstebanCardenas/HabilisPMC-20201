from django.db import models

# Create your models here.

class Usuario(models.Model):
    #Atributos
    cedula = models.BigIntegerField()
    nombre = models.CharField(max_length=50)
    celular = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    #Relaciones

class Paciente(Usuario):
    #Atributos
    edad = models.IntegerField()
    #Relaciones

class Medico(Usuario):
    #Atributos 
    regMedico: models.CharField(max_length=100)
    edad: models.SmallIntegerField()
    especialidad: models.CharField(max_length=120)
    #Relaciones: