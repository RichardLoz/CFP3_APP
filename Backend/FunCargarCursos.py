"""Creo codigo para ejecutar funciones
y que actualiza mi base de datos con los 
datos de los cursos"""

import sqlite3

direccion = "C:/Users/ofern/OneDrive/Escritorio/Proyecto Oucra/proyecto_oucra/base de datos/BDtrabajoUocra.db"


"""Funcion para cargar los cursos a mi BD"""
def cargar_curso(nombre, horas_totales, horas_semanales, turno, direccion= direccion):
    
    conexion = sqlite3.connect(direccion)
    cursor = conexion.cursor()
    
    cursor.execute("SELECT NombreCurso FROM Cursos")
    profesores_existentes = cursor.fetchall()
    
    if (nombre) in profesores_existentes:
        print(f"El curso ya se cargo previamente")
        conexion.close()    
    else:  
        comando = f"""INSERT INTO Cursos (NombreCurso, HorasTotales, HorasSemanales, Turnos)
            VALUES ('{nombre}','{horas_totales}','{horas_semanales}','{turno}') """
        cursor.execute(comando)
        conexion.commit()
        conexion.close()
        print("Se agregaro correctamente el/la docente")
        
"""Funcion para eliminar curso de mi BD"""

def eliminar_curso(id, direccion= direccion):
    conexion = sqlite3.connect(direccion)
    cursor = conexion.cursor()
    
    comando = f"DELETE FROM Cursos WHERE Id={id}"
    cursor.execute(comando)
    conexion.commit()
    conexion.close()
    print("Se elimino el curso de manera correcta")
    
    
# Funcion para mostrar todos los datos.
def mostrar_datos(direccion= direccion):
    conexion = sqlite3.connect(direccion)
    cursor = conexion.cursor()
    
    cursor.execute("SELECT * FROM Cursos")
    valores = cursor.fetchall()
    
    conexion.commit()
    conexion.close()
    
    return valores


""" Funciones para modificar mis valores 
en la BD Cursos"""

# Nombre curso
def modificar_nombre_curso(id, nombre, direccion= direccion):
    conexion = sqlite3.connect(direccion)
    cursor = conexion.cursor()
    
    comando = f"""UPDATE Cursos SET NombreCurso='{nombre}' WHERE Id={id}"""
    cursor.execute(comando)
    conexion.commit()
    conexion.close()
    print("Se modifico correctamente el nombre del curso")
    

#Horas totales
def modificar_horas_totales(id, horas, direccion= direccion):
    conexion = sqlite3.connect(direccion)
    cursor = conexion.cursor()
    
    comando = f"""UPDATE Cursos SET HorasTotales='{horas}' WHERE Id={id}"""
    cursor.execute(comando)
    conexion.commit()
    conexion.close()
    print("Se modifico correctamente las horas totales")
    
    
#Horas Semanales
def modificar_horas_semanales(id, horas_semanales, direccion= direccion):
    conexion = sqlite3.connect(direccion)
    cursor = conexion.cursor()
    
    comando = f"""UPDATE Cursos SET HorasSemanales='{horas_semanales}' WHERE Id={id}"""
    cursor.execute(comando)
    conexion.commit()
    conexion.close()
    print("Se modifico correctamente la cantidad de horas semanales")
    

#Turnos
def modificar_turno(id, disponibilidad, direccion= direccion):
    conexion = sqlite3.connect(direccion)
    cursor = conexion.cursor()
    
    comando = f"""UPDATE Cursos SET Turnos='{disponibilidad}' WHERE Id={id}"""
    cursor.execute(comando)
    conexion.commit()
    conexion.close()
    print("Se modifico correctamente el turno")