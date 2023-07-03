import tkinter as tk

#Ventana ABM Cursos
class VentanaCurso(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("ABM Cursos")
        self.geometry("500x350")
        self.resizable(False, False)
        
        #Frame para contener el ABM
        frame = tk.Frame(self, padx=10, pady=10, relief=tk.SOLID, borderwidth=1)
        frame.grid(sticky="nsew", columnspan=2)
        
        #Nombre
        label_nombre = tk.Label(frame, text="Nombre Curso:")
        label_nombre.grid(row=0, column=0, sticky="w", pady=5)
        entry_nombre = tk.Entry(frame)
        entry_nombre.grid(row=0, column=1)
        
        # Horas
        label_horas = tk.Label(frame, text="Horas Totales Cursada:")
        label_horas.grid(row=1, column=0, sticky="w", pady=5)
        entry_horas = tk.Entry(frame)
        entry_horas.grid(row=1, column=1)
        
        # Horas
        label_horas = tk.Label(frame, text="Horas Semanales:")
        label_horas.grid(row=2, column=0, sticky="w", pady=5)
        entry_horas = tk.Entry(frame)
        entry_horas.grid(row=2, column=1)

        # Turnos
        label_turnos = tk.Label(frame, text="Turnos:")
        label_turnos.grid(row=3, column=0, sticky="w", pady=5)
        entry_turnos = tk.Entry(frame)
        entry_turnos.grid(row=3, column=1)

        # Profesor
        label_profesor = tk.Label(frame, text="Profesor:")
        label_profesor.grid(row=4, column=0, sticky="w", pady=5)
        entry_profesor = tk.Entry(frame)
        entry_profesor.grid(row=4, column=1)
        
        # Botones
        btn_modificar = tk.Button(frame, text="Modificar")
        btn_modificar.grid(row=5, column=0, padx=5, pady=10)
        btn_guardar = tk.Button(frame, text="Guardar")
        btn_guardar.grid(row=5, column=1, padx=5)
        btn_limpiar = tk.Button(frame, text="Limpiar")
        btn_limpiar.grid(row=5, column=2, padx=5)
        
        # Centrar el frame en la ventana principal
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        

