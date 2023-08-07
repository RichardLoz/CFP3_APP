from django.db import models
from administracion.models import Posicion

class Profesor(models.Model):
     nombre = models.CharField(max_length=256)
     apellido = models.CharField(max_length=256)
     edad = models.IntegerField()
     dni = models.CharField(max_length=8)
     turno = models.CharField(max_length=256)
     disponibilidad = models.CharField(max_length=256)
     posicion = models.ForeignKey(Posicion, on_delete=models.CASCADE)
     
     def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    
    
