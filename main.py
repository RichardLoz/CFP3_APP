from dependecias import *

def create_gradient(canvas, width, height, color1, color2):
    # Crear un gradiente lineal vertical en el lienzo
    for y in range(height):
        r = int((color2[0] - color1[0]) * y / height + color1[0])
        g = int((color2[1] - color1[1]) * y / height + color1[1])
        b = int((color2[2] - color1[2]) * y / height + color1[2])
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_line(0, y, width, y+1, fill=color, width=1)
        
def configure_canvas(event, canvas):
    # Configurar el tamaño del lienzo según las dimensiones de la ventana
    canvas.config(width=event.width, height=event.height)


def main():
    
    root = tk.Tk() 
    
    #Icono
    icon_app = 'imagenes/icono.ico'

   #para insertat un titulo en la ventana
    root.title('ACHYC - Administrador de carga horaria y cargos -')
    
    #para incorporar insertar un icono en la ventana
    root.iconbitmap(f"{icon_app}")
    
    #indico que las medidas de las ventanas sean estaticas
    root.resizable(True,True) 
    
    # Crear un lienzo (canvas) que ocupe toda la ventana
    canvas = tk.Canvas(root, width=root.winfo_width(), height=root.winfo_height())
    canvas.grid(row=0, column=0, sticky="nsew")  # Ubicar el lienzo en la celda (0, 0)
    root.grid_rowconfigure(0, weight=1)  # Ajustar el tamaño de la fila a medida que se redimensiona
    root.grid_columnconfigure(0, weight=1)  # Ajustar el tamaño de la columna a medida que se redimensiona

    
    # Colores para el gradiente (en formato RGB)
    color1 = (255, 255, 255)  # Color inicial (blanco)
    color2 = (0, 0, 255)      # Color final (azul)

    # Crear el gradiente en el lienzo
    create_gradient(canvas, root.winfo_width(), root.winfo_height(), color1, color2)

    # insertamos la barra de menu
    barra_menu(root)
    
    # creamos el primer objeto de Frame como contenido del layout
    app = Frame(root)
    app.configure(bg="#f8f8f8")  # Configurar color de fondo del frame
    app.grid(row=0, column=0, sticky="nsew")  # Ubicar el frame en la celda (0, 0)

    # Configurar el tamaño del lienzo cuando se redimensiona la ventana
    #root.bind("<Configure>", lambda event: configure_canvas(event, canvas))

    app.mainloop()

if __name__ =='__main__':
    main()
