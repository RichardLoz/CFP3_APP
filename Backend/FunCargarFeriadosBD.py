"""Creo codigo para ejecutar una funcion
y que actulice mi base de datos con los
feriados correspondiente a los años requeridos."""
#from Api_obtencion_feriados import *
import sqlite3
from datetime import datetime
direccion = "C:/Users/ofern/OneDrive/Escritorio/Proyecto Oucra/proyecto_oucra/base de datos/BDtrabajoUocra.db"

# def cargar_feriados(año_feriados, direccion_bd= direccion):
    
#     feriados = DatosApi(año_feriados)
#     feriados_obtenidos = feriados.feriadosBD()
       
#     conexion = sqlite3.connect(direccion_bd)
#     cursor = conexion.cursor()
    
#     cursor.execute("SELECT FechaFeriado FROM TablaFeriados")
#     feriados_existentes = [fecha[0] for fecha in cursor.fetchall()]
#     feriados_actualizar = []
    
#     for fecha in feriados_obtenidos:
#         if fecha["FechaFeriado"] not in feriados_existentes:
#             feriados_actualizar.append(fecha)
            
#     if len(feriados_actualizar) == 0:
#         print("Los resultados ya se han cargado anteriormente.")
#         conexion.close()
#         return
#     else:
#         for fecha in feriados_actualizar:
#             campo = list(fecha.keys())
#             valor = list(fecha.values())
#             comando = f"INSERT INTO TablaFeriados ({','.join(campo)}) VALUES ({','.join(['?'] * len(valor))})"
#             cursor.execute(comando, valor)
            
#         conexion.commit()
#         conexion.close()
#         print("Los resultados se actualizaron correctamente")


# Funcion para mostrar todos los datos.
def mostrar_datos(direccion= direccion):
    conexion = sqlite3.connect(direccion)
    cursor = conexion.cursor()
    
    cursor.execute("SELECT * FROM TablaFeriados")
    valores = cursor.fetchall()
    
    conexion.commit()
    conexion.close()
    
    return valores


"""Funcion para eliminar feriado de mi BD"""
def eliminar_feriado(id, direccion= direccion):
    conexion = sqlite3.connect(direccion)
    cursor = conexion.cursor()
    
    cursor.execute("SELECT ID_Feriado FROM TablaFeriados")
    feriados_existentes = [elemento[0] for elemento in cursor.fetchall()] 
    
    if id not in feriados_existentes:
        print("El id ingresado no se encuentra en la BD")
        print(id)
        print(type(id))
    else:
        comando = f"DELETE FROM TablaFeriados WHERE ID_Feriado={id}"
        cursor.execute(comando)
        conexion.commit()
        conexion.close()
        print("Se elimino la fecha de manera correcta")


# Funcion para cargar Feriados en mi BD
def cargar_feriado_uocra(fecha, motivo, tipoferiado):
    conexion = sqlite3.connect(direccion)
    cursor = conexion.cursor()
    
    cursor.execute("SELECT FechaFeriado FROM TablaFeriados")
    fechas_existentes = cursor.fetchall()
    
    if (fecha) in fechas_existentes:
        print(f"La fecha ya se cargo previamente")
        conexion.close()    
    else:
        dia = datetime.strptime(fecha, "%d-%m-%Y").date()
        if dia.weekday() == 0:
            dia = "lunes"
        elif dia.weekday() == 1:
            dia = "martes"
        elif dia.weekday() == 2:
            dia = "miercoles"
        elif dia.weekday() == 3:
            dia = "jueves"
        elif dia.weekday() == 4:
            dia = "viernes"
        elif dia.weekday() == 5:
            dia = "sabado"
        elif dia.weekday() == 6:
            dia = "domingo"
            
        comando = f"""INSERT INTO TablaFeriados (FechaFeriado, MotivoFeriado, TipoFeriado, DiaFeriado)
            VALUES ('{fecha}','{motivo}','{tipoferiado}','{dia}') """
        cursor.execute(comando)
        conexion.commit()
        conexion.close()
        print("Se cargo correctamente la fecha")


# Funciones para modificar Feriados 
# funcion para modificar fecha
    # Metodos para modificar:
def modificar_fecha(id, fecha, direccion= direccion):
    conexion = sqlite3.connect(direccion)
    cursor = conexion.cursor()

    cursor.execute("SELECT FechaFeriado FROM TablaFeriados")
    fechas_existentes = cursor.fetchall()

    if (fecha) in fechas_existentes:
        print(f"La fecha ya se ingreso previamente")
        conexion.close()    
    else:
        dia = datetime.strptime(fecha, "%d-%m-%Y").date()
        if dia.weekday() == 0:
            dia = "lunes"
        elif dia.weekday() == 1:
            dia = "martes"
        elif dia.weekday() == 2:
            dia = "miercoles"
        elif dia.weekday() == 3:
            dia = "jueves"
        elif dia.weekday() == 4:
            dia = "viernes"
        elif dia.weekday() == 5:
            dia = "sabado"
        elif dia.weekday() == 6:
            dia = "domingo"    
    
    comando = f"""UPDATE TablaFeriados SET FechaFeriado='{fecha}', DiaFeriado='{dia}' WHERE ID_Feriado={id}"""
    cursor.execute(comando)
    conexion.commit()
    conexion.close()
    print("Se modifico correctamente la fecha")

""" Pruebo mi funcion"""
#cargar_feriados(2022)    