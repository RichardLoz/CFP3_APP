"""Creo codigo para ejecutar funciones
y que actualiza mi base de datos con los 
datos de los profesores"""

import sqlite3

# variable para indicarle la direccion de la Base de Datos.
direccion = "C:/Users/ofern/OneDrive/Escritorio/Proyecto Oucra/proyecto_oucra/base de datos/BDtrabajoUocra.db"

# Funcion para cargar profesores en mi BD
def cargar_profesor(nombre, apellido, tipohora, disponibilidad):
    conexion = sqlite3.connect(direccion)
    cursor = conexion.cursor()
    
    cursor.execute("SELECT Nombre, Apellido FROM Profesores")
    profesores_existentes = cursor.fetchall()
    
    if (nombre, apellido) in profesores_existentes:
        print(f"El/la docente ya se cargo previamente")
        conexion.close()    
    else:  
        comando = f"""INSERT INTO Profesores (Nombre, Apellido, TipoDeHora, DisponibilidadHoraria)
            VALUES ('{nombre}','{apellido}','{tipohora}','{disponibilidad}') """
        cursor.execute(comando)
        conexion.commit()
        conexion.close()
        print("Se agregaro correctamente el/la docente")

"""Pruebo mi funcion"""
#cargar_profesor("Richard","Lozano","catedra","Lunes-Martes-Miercoles")


# Funcion para modificar todo en un profesor determinado a traves de su ID
def modificar_profesor_all(id, nombre, apellido, tipohora, disponibilidad, direccion= direccion):
    conexion = sqlite3.connect(direccion)
    cursor = conexion.cursor()
    
    comando = f"""UPDATE Profesores SET Nombre='{nombre}', Apellido='{apellido}', TipoDeHora='{tipohora}', 
        DisponibilidadHoraria='{disponibilidad}' WHERE Id={id}"""
    cursor.execute(comando)
    conexion.commit()
    conexion.close()
    print("Se modificaron correctamente las fechas")


# Funcion para mostrar todos los datos.
def mostrar_datos(direccion= direccion):
    conexion = sqlite3.connect(direccion)
    cursor = conexion.cursor()
    
    cursor.execute("SELECT * FROM Profesores")
    valores = cursor.fetchall()
    
    conexion.commit()
    conexion.close()
    
    return valores

"""Pruebo mi funcion"""
#modificar_profesor_all(1,"Richards","Loz","Catedra","Lunes-Miercoles-Viernes")

def eliminar_profesor(id, direccion= direccion):
    conexion = sqlite3.connect(direccion)
    cursor = conexion.cursor()
    
    comando = f"DELETE FROM Profesores WHERE Id={id}"
    cursor.execute(comando)
    conexion.commit()
    conexion.close()
    print("Se elimino la/el docente de manera correcta")
    
"""Pruebo mi funcion"""
#eliminar_profesor(5)


def modificar_profesor_nombre(id, nombre, direccion= direccion):
    conexion = sqlite3.connect(direccion)
    cursor = conexion.cursor()
    
    comando = f"""UPDATE Profesores SET Nombre='{nombre}' WHERE Id={id}"""
    cursor.execute(comando)
    conexion.commit()
    conexion.close()
    print("Se modifico correctamente el nombre")
    
"""pruebo mi funcion"""
#modificar_profesor_nombre(4,"Pepe")

# Funcion para modificar solo el apellido
def modificar_profesor_apellido(id, apellido, direccion= direccion):
    conexion = sqlite3.connect(direccion)
    cursor = conexion.cursor()
    
    comando = f"""UPDATE Profesores SET Apellido='{apellido}' WHERE Id={id}"""
    cursor.execute(comando)
    conexion.commit()
    conexion.close()
    print("Se modifico correctamente el apellido")
    
"""pruebo mi funcion"""
#modificar_profesor_apellido(4,"fernandez")

# Funcion para modificar solo el tipo de hora
def modificar_profesor_tipohora(id, tipohora, direccion= direccion):
    conexion = sqlite3.connect(direccion)
    cursor = conexion.cursor()
    
    comando = f"""UPDATE Profesores SET TipoDeHora='{tipohora}' WHERE Id={id}"""
    cursor.execute(comando)
    conexion.commit()
    conexion.close()
    print("Se modifico correctamente el tipo de hora")
    
"""pruebo mi funcion"""
#modificar_profesor_tipohora(4,"practica")

# Funcion para modificar solo la disponibilidad
def modificar_profesor_disponibilidad(id, disponibilidad, direccion= direccion):
    conexion = sqlite3.connect(direccion)
    cursor = conexion.cursor()
    
    comando = f"""UPDATE Profesores SET DisponibilidadHoraria='{disponibilidad}' WHERE Id={id}"""
    cursor.execute(comando)
    conexion.commit()
    conexion.close()
    print("Se modifico correctamente la disponibilidad horaria")
    
"""pruebo mi funcion"""
#modificar_profesor_disponibilidad(4,"jueves")