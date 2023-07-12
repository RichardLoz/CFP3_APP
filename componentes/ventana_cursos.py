import tkinter as tk
from tkinter import ttk
from Backend.FunCargarCursos import *


class VentanaCurso2(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("ABM de Curso")
        self.geometry("550x380")
        self.resizable(False, False)

        self.tree = ttk.Treeview(self) ##
        
        # Nombre Curso
        label_nombre = tk.Label(self, text="Nombre del Curso:")
        label_nombre.grid(row=0 , column=0 )
        entry_nombre = tk.Entry(self)
        self.nombre = entry_nombre
        entry_nombre.grid(row=0 , column=1 )

        # Horas Totales
        label_horas_totales = tk.Label(self, text="Horas Totales:")
        label_horas_totales.grid(row=1 , column=0 )
        entry_horas_totales = tk.Entry(self)
        self.horas_totales = entry_horas_totales
        entry_horas_totales.grid(row=1 , column=1 )

        # Horas Semanales
        label_horas_semanales = tk.Label(self, text="Horas Semanales:")
        label_horas_semanales.grid(row=2 , column=0)
        entry_horas_semanales = tk.Entry(self)
        self.horas_semanales = entry_horas_semanales
        entry_horas_semanales.grid(row=2 , column=1 )

        # Disponibilidad Horaria
        label_turno = tk.Label(self, text="Turno:")
        label_turno.grid(row=3 , column=0)

        # Modificar profesores
        label_modificar = tk.Label(self,text="Ingrese Id")
        label_modificar.grid(row=5,column=0)
        entry_id = tk.Entry(self)
        self.id = entry_id
        entry_id.grid(row=5, column=1)
        
        # Botones
        btn_guardar = tk.Button(self, text="Guardar", command=self.guardar)
        btn_guardar.grid(row=4, column=0 )
        btn_actualizar = tk.Button(self, text="Actualizar", command= self.actualizar)
        btn_actualizar.grid(row=4 , column=1 )
        btn_eliminar = tk.Button(self, text="Eliminar", command= self.eliminar)
        btn_eliminar.grid(row=5 , column=3 )
        btn_modificar = tk.Button(self, text="Modificar", command= self.modificar)
        btn_modificar.grid(row=5, column=2)
        
        
        ## Checkbutton - Botón de selección que puede estar activado o desactivado. 
        self.mañana = tk.IntVar() #  Creo una variable IntVar() que será utilizada para almacenar el estado del Checkbutton asociado al día "LUNES".
        mañana_check = ttk.Checkbutton(self, text="MAÑANA", variable=self.mañana) # Creo el Checkbutton para el "LUNES". Utilizo ttk.Checkbutton() para crear el widget, asigno nombre "LUNES" a traves de text, lo vinculo a variable lunes_estado. 
        mañana_check.grid(row=3, column=1, sticky=tk.E) # Indico en la posicion que se va a encontrar el check. Uso sticky=tk.E para alinear el Checkbutton a la derecha de su celda en la cuadrícula.
        
        self.tarde = tk.IntVar()
        tarde_check = ttk.Checkbutton(self, text="TARDE", variable=self.tarde)
        tarde_check.grid(row=3, column=2)
        
        self.noche = tk.IntVar()
        noche_check = ttk.Checkbutton(self, text="NOCHE", variable=self.noche)
        noche_check.grid(row=3, column=3)
        
       
        #Treeview para mostrar los datos en forma de tabla
        self.tree["columns"]=("Id","Nombre Curso","Hs Totales","Hs Semanal","Turno")  #Se define las columnas del Treeview, especificando sus identificadores.
        
        self.tree.column("#0", width=0, stretch=tk.NO)             # Se configura la columna "#0", es la columna de la estructura jerárquica del Treeview. 
        self.tree.column("Id", width=50, anchor=tk.CENTER)         # Se establece un ancho de 0 y se desactiva el estiramiento haciendola no visible.
        self.tree.column("Nombre Curso", width=100, anchor=tk.CENTER)    # Estas líneas configuran las columnas restantes del Treeview. 
        self.tree.column("Hs Totales", width=100, anchor=tk.CENTER)  # Cada columna se identifica por su nombre y se establece su ancho(width) y ubicacion (anchor)
        self.tree.column("Hs Semanal", width=100, anchor=tk.CENTER) 
        self.tree.column("Turno", width=200, anchor=tk.CENTER)
        
        self.tree.heading("#0", text="",anchor=tk.CENTER)              # Estas líneas configuran los encabezados de columna del Treeview
        self.tree.heading("Id", text="Id", anchor=tk.CENTER)           # Cada encabezado se establece mediante el método heading(), 
        self.tree.heading("Nombre Curso", text="Nombre Curso", anchor=tk.CENTER)   # Especificando el identificador de la columna y el texto a mostrar en el encabezado.
        self.tree.heading("Hs Totales", text="Hs Totales", anchor=tk.CENTER)
        self.tree.heading("Hs Semanal", text="Hs Semanal", anchor=tk.CENTER)
        self.tree.heading("Turno", text="Turno", anchor=tk.CENTER)
        
        self.tree.grid(row=8, columnspan=7) # Esta línea coloca el Treeview en la cuadrícula (grid) de la interfaz gráfica. 
        
        
    #Metodo actualizar para mostrar los ultimos datos
    def actualizar(self):
        
        valores_nuevos = mostrar_datos()
        valores_cargados = [self.tree.item(item)["values"][0] for item in self.tree.get_children()]
        
        for i in valores_nuevos:
            if i[0] not in valores_cargados:
                self.tree.insert("",tk.END, values= i)
                
    
    # Metodo para guardar    
    def guardar(self):
        
        self.check()
        nombre = self.nombre.get()
        horas_totales =  self.horas_totales.get()
        horas_semanales = self.horas_semanales.get()
        turno = self.check()
        
        if nombre or horas_totales or horas_semanales or turno:
            cargar_curso(nombre, horas_totales, horas_semanales, turno)
        else:
            print("No se ingreso ningun valor para guardar")
    
    
    # Metodo para modificar cursos cargados
    def modificar(self):
        id = self.id.get()    
        datos_ingresados = False
        
        if id: 
            if self.nombre.get():
                modificar_nombre_curso(id,self.nombre.get())
                datos_ingresados = True
            if self.horas_totales.get():
                modificar_horas_totales(id,self.horas_totales.get())
                datos_ingresados = True
            if self.horas_semanales.get():
                modificar_horas_semanales(id,self.horas_semanales.get())
                datos_ingresados = True
            if self.mañana.get() or self.tarde.get() or self.noche.get():
                modificar_turno(id,self.check())
                datos_ingresados = True
            else:
                print("No se selecciono ningun valor a modificar")
        else:
            print("Por favor ingrese un ID para modificar un valor")
        
        if datos_ingresados == True:
            self.tree.delete(*self.tree.get_children())


    # Metodo para verificar si esta seleccionada la casilla, a que turno corresponde
    # almacenarlo en una lista para cargarlo en la BD
    def check(self):
        lista = []

        if self.mañana.get() == 1:
            lista.append("mañana")
            
        if self.tarde.get() == 1:
            lista.append("tarde")
            
        if self.noche.get() == 1:
            lista.append("noche")

        #Verifico si hay datos en lista y transformo mi lista en un str para mostrarlo con la separacion "-"
        if lista:
            dias = ""
            for i in lista:
                maximo = len(lista)
                if lista.index(i) == maximo -1:
                    dias += i
                else:
                    dias += f"{i}-"
        
        if len(lista) != 0:
            return dias
        else:
            return lista
            

    #Metodo para eliminar un Curso
    def eliminar(self):
        id = self.id.get()
        print(id)
        
        if id:
            eliminar_curso(id)
        else:
            print("No se ingreso ID")
        
        self.tree.delete(*self.tree.get_children())