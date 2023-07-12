#TODO: Trabajando con base de datos

#1- Importar modulo sqlite3
import sqlite3




#Conectar y crear base de datos
def conectar():
    #Se establece una conexion con la base de datos.
    con = sqlite3.connect("prueba.db")
    #Se crea un objeto cursor el cual se utiliza para ejecutar comandos SQL en la base de datos.
    cursor = con.cursor()
    #La funcion retorna los objetos "con" y "cursor" permitiendo a quien la llame realizar operacioens en la DB
    return con, cursor

#Crear tabla
# Los parametros "conexion" y "cursor" se utilizan para establecer la conexión a la base de datos y realizar operaciones en ella.
def crear_tabla(conexion, cursor):
    #Sentencia para crear la tabla
    sentencia = """
        CREATE TABLE IF NOT EXISTS usuarios
        (ID INTEGER PRIMARY KEY NOT NULL,
        USUARIO TEXT NOT NULL,
        EMAIL TEXT NOT NULL,
        CLAVE TEXT NOT NULL
        )
    """
    #Ejecuta la sentencia SQL utilizando el cursor proporcionado como parámetro.
    cursor.execute(sentencia)
    #Cierra la conexión a la base de datos
    conexion.close()
    print("La tabla se creo correctamente")
    
#Insertar un registro
def insertar_datos(conexion, cursor):
    sentencia = """
        INSERT INTO usuarios(ID, USUARIO, EMAIL, CLAVE) VALUES (1, "Roberto", "roberto@cfp.com", "humberto")
    """
    #Ejecuta la sentencia SQL utilizando el cursor proporcionado como parámetro.
    cursor.execute(sentencia)
    #confirma los cambios realizados en la base de datos
    conexion.commit()
    #Cierra la conexión a la base de datos
    conexion.close()

#Se evalua si el archivo se ejecuta directamente o si se importa como modulo en otro archivo, es una convención usar esta estructura para definir la logica principal de un programa.
if __name__ == '__main__':
    #Desempaquetado de la tupla que retorna conectar() para asignarlo a las variables "con" y "cursor"
    con, cursor = conectar()
    #En las variables "con" y "cursor" tenemos los valores que retorno la funcion conectar() que se usaran como argumentos en las funciones crear_tabla() y insertar_datos()
    crear_tabla(con, cursor)
    insertar_datos(con, cursor)