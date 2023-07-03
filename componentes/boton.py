import tkinter as tk

class Boton(tk.Button):
    def __init__(self, parent, text, command=None):
        super().__init__(parent, text=text, command=command)
        self.pack()