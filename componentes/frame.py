import tkinter as tk
from componentes.ventana_profesor import VentanaProfesor
from componentes.ventana_cursos import VentanaCurso2
from componentes.calculadora_xavi import Calculadora
from componentes.ventana_feriados import VentanaFeriados

# clase
class Frame(tk.Frame):
    def __init__(self, root=None ):
        super().__init__(root, width = 824, height= 568 )
        self.root = root
        self.grid()
        self['bg'] = '#f8f8f8'
        
    #Configuracion del espaciado y tamano de los botones
        padding_x = 10
        padding_y = 10
        button_width = 30
        button_height = 5

    #Botones ventana principal
        self.btn_cursos = tk.Button(self, text="Cursos", command=self.abrir_cursos, width=button_width, height=button_height)
        self.btn_cursos.grid(row=0, column=0, padx=padding_x, pady=padding_y)
        
        self.btn_profesores = tk.Button(self, text="Profesores", command=self.abrir_profesores, width=button_width, height=button_height)
        self.btn_profesores.grid(row=0, column=1, padx=padding_x, pady=padding_y)
        
        self.btn_calculadora_manual = tk.Button(self, text="Calculadora Manual", command=self.abrir_calculadora_manual, width=button_width, height=button_height)
        self.btn_calculadora_manual.grid(row=0, column=2, padx=padding_x, pady=padding_y)
        
        self.btn_carga_feriados = tk.Button(self, text="Feriados / Dias no cursables Uocra", command=self.abrir_carga_feriados, width=button_width, height=button_height)
        self.btn_carga_feriados.grid(row=1, column=1, padx=padding_x, pady=padding_y)
    
    def abrir_cursos(self):
        ventana = VentanaCurso2(self)
    
    def abrir_profesores(self):
        ventana = VentanaProfesor(self)
    
    def abrir_calculadora_manual(self):
        ventana = Calculadora(self)
    
    def abrir_carga_feriados(self):
        ventana = VentanaFeriados(self)