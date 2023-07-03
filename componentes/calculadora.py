import tkinter as tk

class Calculadora(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Calculadora")
        self.geometry("500x350")
        self.resizable(False, False)
        
        #Frame para contener el ABM
        frame = tk.Frame(self, padx=15, pady=15, relief=tk.SOLID, borderwidth=1)
        frame.grid(sticky="nsew", columnspan=6)
        
        #fecha de inicio
        label_nombre = tk.Label(frame, text="Fecha de inicio:")
        label_nombre.grid(row=0, column=0, sticky="w", pady=5)
        entry_nombre = tk.Entry(frame)
        entry_nombre.grid(row=0, column=1)
        
        # Total de las horas
        label_horas = tk.Label(frame, text="Total de horas del curso:")
        label_horas.grid(row=1, column=0, sticky="w", pady=5)
        entry_horas = tk.Entry(frame)
        entry_horas.grid(row=1, column=1)
        
        # Tipo de horas a cursar
        label_horas = tk.Label(frame, text="Tipo de hora:")
        label_horas.grid(row=2, column=0, sticky="w", pady=5)
        entry_horas = tk.Entry(frame)
        entry_horas.grid(row=2, column=1)

        # Horas reloj
        label_turnos = tk.Label(frame, text="Total de horas reloj semanal:")
        label_turnos.grid(row=3, column=0, sticky="w", pady=5)
        entry_turnos = tk.Entry(frame)
        entry_turnos.grid(row=3, column=1)

        # Dias de disponibilidad
        #revisar el codigo de color de los botones
        label_profesor = tk.Label(frame, text="Marcar los dias disponibles:")
        label_profesor.grid(row=4, column=0, sticky="w", pady=5)
        def toggle_button_color(button):
            current_bg = button["bg"]
            new_bg = "blue" if current_bg != "blue" else ""
            button.config(bg=new_bg)
            days_of_week = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

            for i, day in enumerate(days_of_week):
                button = tk.Button(frame, text=day, command=lambda d=day: button_click(d))
                button.grid(row=5, column=1, padx=5, pady=5)
            
        # Botones
        btn_modificar = tk.Button(frame, text="Modificar")
        btn_modificar.grid(row=8, column=0, padx=5, pady=10)
        btn_guardar = tk.Button(frame, text="Guardar")
        btn_guardar.grid(row=8, column=1, padx=5)
        btn_limpiar = tk.Button(frame, text="Limpiar")
        btn_limpiar.grid(row=8, column=2, padx=5)
        
        # Centrar el frame en la ventana principal
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        