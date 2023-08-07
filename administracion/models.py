from django.db import models

class Posicion(models.Model):
    nombre = models.CharField(max_length=256)
    hora = models.FloatField()
    
    def __str__(self):
        return self.nombre


class Curso(models.Model):
    nombre = models.CharField(max_length=256)
    horas_totales = models.IntegerField()
    turno = models.CharField(max_length=256)
    profesor = models.ManyToManyField('profesor.Profesor')
    
    def __str__(self):
        return self.nombre
    

class Feriado(models.Model):
    nombre = models.CharField(max_length=256)
    motivo = models.CharField(max_length=256)
    fecha = models.DateField()
    
    def __str__(self):
        return self.nombre
    
       