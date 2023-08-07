from django.shortcuts import render, redirect
from .models import Profesor
from administracion.models import Posicion

def list_profesores(request):
    profesores = Profesor.objects.all()
    posiciones = Posicion.objects.all()
    return render(request, 'profesores.html', {'profesores':profesores, 'posiciones':posiciones})

def store_profesor(request):
    nombre =  request.POST["nombre"]
    apellido = request.POST["apellido"]
    edad = request.POST["edad"]
    dni = request.POST["dni"]
    turno = request.POST["turno"]
    disponibilidad = request.POST["disponibilidad"]
    posicion_id = request.POST["posicion_id"]
    posicion = Posicion.objects.get(id=posicion_id)
    profesor = Profesor(nombre=nombre, apellido=apellido, edad=edad, dni=dni, turno=turno, disponibilidad=disponibilidad, posicion=posicion)
    profesor.save()
    return redirect('/profesores/')
    

def update_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    nombre =  request.POST["nombre"]
    apellido = request.POST["apellido"]
    edad = request.POST["edad"]
    dni = request.POST["dni"]
    turno = request.POST["turno"]
    disponibilidad = request.POST["disponibilidad"]
    posicion_id = request.POST["posicion_id"]
    posicion = Posicion.objects.get(id=posicion_id)
    profesor.nombre = nombre
    profesor.apellido = apellido
    profesor.edad = edad
    profesor.dni = dni
    profesor.turno = turno
    profesor.disponibilidad = disponibilidad
    profesor.posicion = posicion
    profesor.save()
    return redirect('/profesores/')
    
    
def delete_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    return redirect('/profesores/')
    
    
    
    