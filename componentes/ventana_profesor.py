import tkinter as tk
from tkinter import ttk
from Backend.FunCargarProfesor import *


class VentanaProfesor(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("ABM de Profesores")
        self.geometry("550x380")
        self.resizable(False, False)

        self.tree = ttk.Treeview(self) ##
        
        # Nombre
        label_nombre = tk.Label(self, text="Nombre:")
        label_nombre.grid(row=0 , column=0 )
        entry_nombre = tk.Entry(self)
        self.nombre = entry_nombre
        entry_nombre.grid(row=0 , column=1 )

        # Apellido
        label_apellido = tk.Label(self, text="Apellido:")
        label_apellido.grid(row=1 , column=0 )
        entry_apellido = tk.Entry(self)
        self.apellido = entry_apellido
        entry_apellido.grid(row=1 , column=1 )

        # Tipo Hora
        label_tipo_hora = tk.Label(self, text="Tipo Hora:")
        label_tipo_hora.grid(row=2 , column=0)
        entry_tipo_hora = tk.Entry(self)
        self.tipo_hora = entry_tipo_hora
        entry_tipo_hora.grid(row=2 , column=1 )

        # Disponibilidad Horaria
        label_disp_horaria = tk.Label(self, text="Disponibilidad Horaria:")
        label_disp_horaria.grid(row=3 , column=0)

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
        self.lunes_estado = tk.IntVar() #  Creo una variable IntVar() que será utilizada para almacenar el estado del Checkbutton asociado al día "LUNES".
        lunes_check = ttk.Checkbutton(self, text="LUNES", variable=self.lunes_estado) # Creo el Checkbutton para el "LUNES". Utilizo ttk.Checkbutton() para crear el widget, asigno nombre "LUNES" a traves de text, lo vinculo a variable lunes_estado. 
        lunes_check.grid(row=3, column=1, sticky=tk.E) # Indico en la posicion que se va a encontrar el check. Uso sticky=tk.E para alinear el Checkbutton a la derecha de su celda en la cuadrícula.
        
        self.martes_estado = tk.IntVar()
        martes_check = ttk.Checkbutton(self, text="MARTES", variable=self.martes_estado)
        martes_check.grid(row=3, column=2)
        
        self.miercoles_estado = tk.IntVar()
        miercoles_check = ttk.Checkbutton(self, text="MIERCOLES", variable=self.miercoles_estado)
        miercoles_check.grid(row=3, column=3)
        
        self.jueves_estado = tk.IntVar()
        jueves_check = ttk.Checkbutton(self, text="JUEVES", variable=self.jueves_estado)
        jueves_check.grid(row=3, column=4)
        
        self.viernes_estado = tk.IntVar()
        viernes_check = ttk.Checkbutton(self, text="VIERNES", variable=self.viernes_estado)
        viernes_check.grid(row=3, column=5)
        
       
        #Treeview para mostrar los datos en forma de tabla
        self.tree["columns"]=("Id","Nombre","Apellido","TipoDeHora","DisponibilidadHoraria")  #Se define las columnas del Treeview, especificando sus identificadores.
        
        self.tree.column("#0", width=0, stretch=tk.NO)             # Se configura la columna "#0", es la columna de la estructura jerárquica del Treeview. 
        self.tree.column("Id", width=50, anchor=tk.CENTER)         # Se establece un ancho de 0 y se desactiva el estiramiento haciendola no visible.
        self.tree.column("Nombre", width=100, anchor=tk.CENTER)    # Estas líneas configuran las columnas restantes del Treeview. 
        self.tree.column("Apellido", width=100, anchor=tk.CENTER)  # Cada columna se identifica por su nombre y se establece su ancho(width) y ubicacion (anchor)
        self.tree.column("TipoDeHora", width=100, anchor=tk.CENTER) 
        self.tree.column("DisponibilidadHoraria", width=200, anchor=tk.CENTER)
        
        self.tree.heading("#0", text="",anchor=tk.CENTER)              # Estas líneas configuran los encabezados de columna del Treeview
        self.tree.heading("Id", text="Id", anchor=tk.CENTER)           # Cada encabezado se establece mediante el método heading(), 
        self.tree.heading("Nombre", text="Nombre", anchor=tk.CENTER)   # Especificando el identificador de la columna y el texto a mostrar en el encabezado.
        self.tree.heading("Apellido", text="Apellido", anchor=tk.CENTER)
        self.tree.heading("TipoDeHora", text="TipoDeHora", anchor=tk.CENTER)
        self.tree.heading("DisponibilidadHoraria", text="DisponibilidadHoraria", anchor=tk.CENTER)
        
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
        apellido =  self.apellido.get()
        tipo_hora = self.tipo_hora.get()
        
        if nombre or apellido or tipo_hora or self.check() != "vacio":
            cargar_profesor(nombre, apellido, tipo_hora, self.check())
        else:
            print("No se ingreso ningun valor")
    
    # Metodo para modificar profesores cargados
    def modificar(self):
        id = self.id.get()    
        
        if id:         
            if self.nombre.get():
                modificar_profesor_nombre(id,self.nombre.get())
            if self.apellido.get():
                modificar_profesor_apellido(id,self.apellido.get())
            if self.tipo_hora.get():
                modificar_profesor_tipohora(id,self.tipo_hora.get())
            if self.lunes_estado.get() or self.martes_estado.get() or self.miercoles_estado.get() or self.jueves_estado.get() or self.viernes_estado.get():
                modificar_profesor_disponibilidad(id,self.check())
            
            self.tree.delete(*self.tree.get_children())
        else:
            print("No se ingreso ningun ID")
            
    # Metodo para verificar si esta seleccionada la casilla, a que dia corresponde
    # almacenarlo en una lista para cargarlo en la BD
    def check(self):
        lista = []

        if self.lunes_estado.get() == 1:
            lista.append("lunes")
            
        if self.martes_estado.get() == 1:
            lista.append("martes")
            
        if self.miercoles_estado.get() == 1:
            lista.append("miercoles")
            
        if self.jueves_estado.get() == 1:
            lista.append("jueves")
            
        if self.viernes_estado.get() == 1:
            lista.append("viernes")
        
        #Verifico si hay datos en lista y transformo mi lista en un str para mostrarlo con la separacion "-"
        if lista:
            dias = ""
            for i in lista:
                maximo = len(lista)
                if lista.index(i) == maximo -1:
                    dias += i
                else:
                    dias += f"{i}-"
     
            return dias                     
        else:
            lista = "vacio"
            return lista
        
        # if len(lista) != 0:
        #     return lista
        # else:
        #     lista = "vacio" 
        #     return lista
         
    #Metodo para eliminar un profesor
    def eliminar(self):
        id = self.id.get()
        
        if id:
            eliminar_profesor(id)
        else:
            print("No se ingreso ID")
        
        self.tree.delete(*self.tree.get_children())