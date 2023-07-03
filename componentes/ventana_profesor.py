import tkinter as tk

#Ventana ABM Profesores
class VentanaProfesor(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("ABM de Profesores")
        self.geometry("500x350")
        self.resizable(False, False)
        
        #Frame para contener el ABM
        frame = tk.Frame(self, padx=10, pady=10, relief=tk.SOLID, borderwidth=1)
        frame.grid(sticky="nsew", columnspan=2)

        # Nombre
        label_nombre = tk.Label(frame, text="Nombre:")
        label_nombre.grid(row=0 , column=0, sticky="w", pady=5 )
        entry_nombre = tk.Entry(frame)
        entry_nombre.grid(row=0 , column=1 )

        # Apellido
        label_apellido = tk.Label(frame, text="Apellido:")
        label_apellido.grid(row=1 , column=0, sticky="w", pady=5 )
        entry_apellido = tk.Entry(frame)
        entry_apellido.grid(row=1 , column=1 )

        # Tipo Hora
        label_tipo_hora = tk.Label(frame, text="Tipo Hora:")
        label_tipo_hora.grid(row=2 , column=0, sticky="w", pady=5)
        entry_tipo_hora = tk.Entry(frame)
        entry_tipo_hora.grid(row=2 , column=1 )

        # Disponibilidad Horaria
        label_disp_horaria = tk.Label(frame, text="Disponibilidad Horaria:")
        label_disp_horaria.grid(row=3 , column=0, sticky="w", pady=5)
        entry_disp_horaria = tk.Entry(frame)
        entry_disp_horaria.grid(row=3 , column=1)

        # Botones
        btn_guardar = tk.Button(frame, text="Guardar")
        btn_guardar.grid(row=4, column=0, padx=5, pady=10 )
        btn_modificar = tk.Button(frame, text="Modificar")
        btn_modificar.grid(row=4 , column=1, padx=5 )
        btn_limpiar = tk.Button(frame, text="Limpiar")
        btn_limpiar.grid(row=4 , column=2, padx=5 )
        
        
        # Centrar el frame en la ventana principal
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)