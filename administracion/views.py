from django.shortcuts import render, redirect
from .models import Curso
from profesor.models import Profesor



def index_view(request):
    return render(request, 'index.html')


def list_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos':cursos})


def store_curso(request):
    nombre = request.POST["nombre"]
    horas_totales = request.POST["horas_totales"]
    turno = request.POST["turno"]
    profesor_id = request.POST["profesor_id"]
    profesor = Profesor.objects.get(id=profesor_id)
    curso = Curso(nombre=nombre, horas_totales=horas_totales, turno=turno, profesor=profesor)
    curso.save()
    return redirect('/cursos/')


def update_curso(request):
    curso = Curso.objects.get(id=id)
    nombre = request.POST["nombre"]
    horas_totales = request.POST["horas_totales"]
    turno = request.POST["turno"]
    profesor_id = request.POST["profesor_id"]
    profesor = Profesor.objects.get(id=profesor_id)
    curso.nombre = nombre
    curso.horas_totales = horas_totales
    curso.turno = turno
    curso.profesor = profesor
    curso.save()
    return redirect('/cursos/')


def delete_curso(request):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect('/cursos/')