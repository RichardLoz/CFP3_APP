import tkinter as tk
from tkinter import ttk
from Backend.Api_obtencion_feriados import *
from Backend.FunCargarFeriadosBD import *
from tkcalendar import DateEntry ## pip install tkcalendar


class VentanaFeriados(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("ABM Feriados y Dias No Cursables")
        self.geometry("600x380")
        self.resizable(False, False)

        
        #Ingresar dia no cursable
        label_fecha_uocra = tk.Label(self, text="Seleccione dia no cursable:")
        label_fecha_uocra.grid(row=0 , column=0, sticky="ew" )
        self.dia_no_cursable = DateEntry(self, locale= 'es_ES')
        self.dia_no_cursable.grid(row=0 , column=1, sticky="ew")


        # Motivo Feriado
        label_motivo_uocra = tk.Label(self, text="Motivo :")
        label_motivo_uocra.grid(row=1 , column=0 )
        entry_motivo_uocra = tk.Entry(self)
        self.motivo_uocra = entry_motivo_uocra
        entry_motivo_uocra.grid(row=1 , column=1)


        #Tipo Feriado
        label_tipo_feriado = tk.Label(self, text="Tipo de Feriado :")
        label_tipo_feriado.grid(row=2, column=0)
        entry_tipo_feriado = tk.Entry(self)
        self.tipo_feriado = entry_tipo_feriado
        entry_tipo_feriado.grid(row=2, column=1)
        
        # Ingresar ID
        label_modificar = tk.Label(self,text="Ingrese Id :")
        label_modificar.grid(row=5,column=0)
        entry_id = tk.Entry(self)
        self.id = entry_id
        entry_id.grid(row=5, column=1)
 
        # Actualizar año
        label_año = tk.Label(self,text="Ingresar año para actualizar feriados")
        label_año.grid(row=0, column=3, sticky="ew")
        entry_año = tk.Entry(self)
        self.entry_año = entry_año
        entry_año.grid(row=1, column=3)
        
        # Botones
        btn_guardar = tk.Button(self, text="Guardar", command=self.guardar)
        btn_guardar.grid(row=3, column=1, sticky="ew" )
        btn_actualizar = tk.Button(self, text="Actualizar", command= self.actualizar)
        btn_actualizar.grid(row=5 , column=3 )
        btn_eliminar = tk.Button(self, text="Eliminar", command=self.eliminar)
        btn_eliminar.grid(row=5 , column=5 )
        btn_modificar = tk.Button(self, text="Modificar", command= self.modificar )
        btn_modificar.grid(row=5, column=2)
        btn_año = tk.Button(self, text="Agregar Año", command="")
        btn_año.grid(row=2, column=3)
          
        #Treeview para mostrar los datos en forma de tabla
        self.tree = ttk.Treeview(self) 
        
        self.tree["columns"]=("Id","FechaFeriado","MotivoFeriado","TipoFeriado","DiaFeriado")  #Se define las columnas del Treeview, especificando sus identificadores.
        
        self.tree.column("#0", width=0, stretch=tk.NO)             # Se configura la columna "#0", es la columna de la estructura jerárquica del Treeview. 
        self.tree.column("Id", width=50, anchor=tk.CENTER)         # Se establece un ancho de 0 y se desactiva el estiramiento haciendola no visible.
        self.tree.column("FechaFeriado", width=100, anchor=tk.CENTER)    # Estas líneas configuran las columnas restantes del Treeview. 
        self.tree.column("MotivoFeriado", width=200, anchor=tk.CENTER)  # Cada columna se identifica por su nombre y se establece su ancho(width) y ubicacion (anchor)
        self.tree.column("TipoFeriado", width=100, anchor=tk.CENTER) 
        self.tree.column("DiaFeriado", width=150, anchor=tk.CENTER)
        
        self.tree.heading("#0", text="",anchor=tk.CENTER)              # Estas líneas configuran los encabezados de columna del Treeview
        self.tree.heading("Id", text="Id", anchor=tk.CENTER)           # Cada encabezado se establece mediante el método heading(), 
        self.tree.heading("FechaFeriado", text="FechaFeriado", anchor=tk.CENTER)   # Especificando el identificador de la columna y el texto a mostrar en el encabezado.
        self.tree.heading("MotivoFeriado", text="MotivoFeriado", anchor=tk.CENTER)
        self.tree.heading("TipoFeriado", text="TipoFeriado", anchor=tk.CENTER)
        self.tree.heading("DiaFeriado", text="DiaFeriado", anchor=tk.CENTER)
        
        self.tree.grid(row=8, columnspan=8) # Esta línea coloca el Treeview en la cuadrícula (grid) de la interfaz gráfica. 
        
    
    #Metodo para obtener la fecha STR
    def dia_selecionado_str(self):
        fecha = self.dia_no_cursable.get()
        fecha = datetime.strptime(fecha, "%d/%m/%y").date()
        fecha = fecha.strftime("%d-%m-%Y")
        return fecha
           
    #Metodo actualizar para mostrar los ultimos datos
    def actualizar(self):
        
        valores_nuevos = mostrar_datos()
        valores_cargados = [self.tree.item(item)["values"][0] for item in self.tree.get_children()]
        
        for i in valores_nuevos:
            if i[0] not in valores_cargados:
                self.tree.insert("",tk.END, values= i)
                
    
    
    # Metodo para guardar nueva fecha    
    def guardar(self):
        fecha = self.dia_selecionado_str()
        motivo =  self.motivo_uocra.get()
        tipo = self.tipo_feriado.get()
        
        cargas = {"'Fecha'" : fecha, "'Motivo feriado'" : motivo, "'Tipo de Feriado'" : tipo}
        faltantes = ""
        
        if fecha and motivo and tipo:
            cargar_feriado_uocra(fecha, motivo, tipo)
        else:
            for clave, valor in cargas.items():
                if not valor:
                    faltantes = clave + faltantes
                    
            if len(faltantes) > 1:
                print(f"No se ingresaron los valores {faltantes}")
            else:
                print(f"No se ingreso {faltantes}")
    
    
    # Metodo para modificar cursos cargados
    def modificar(self):
        id = self.id.get()    
        fecha = self.dia_selecionado_str()
        datos_ingresados = False
        
        if id: 
            id = int(id)
            if fecha:
                modificar_fecha(id,fecha)
                datos_ingresados = True
            # if self.motivo_uocra.get():
            #     modificar_horas_totales(id,self.motivo_uocra.get())
            #     datos_ingresados = True
            # if self.tipo_feriado.get():
            #     modificar_horas_semanales(id,self.tipo_feriado.get())
            #     datos_ingresados = True
            else:
                
                print("No se selecciono ningun valor a modificar")
        else:
            print("Por favor ingrese un ID para modificar un valor")
        
        if datos_ingresados == True:
            self.tree.delete(*self.tree.get_children())


    #Metodo para eliminar una Fecha
    def eliminar(self):
        id = self.id.get()
        print(id)
        
        if id:
            id = int(id)
            eliminar_feriado(id)
        else:
            print("No se ingreso ID")
        
        self.tree.delete(*self.tree.get_children())