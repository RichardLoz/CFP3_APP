import tkinter as tk

#barra menu desplegable
def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu) #En esta parte saque width=300, height = 300 ya que no son necesarios
    
    #Creacion de titulos de barra menu
    menu_archivo_label = "Archivo"
    menu_opciones_label = "Opciones"
    menu_ayuda_label = "Ayuda"
    
    #creamos menu archivo en la barra
    menu_archivo = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label =f"{menu_archivo_label}", menu = menu_archivo)

    menu_archivo.add_command(label='nuevo')
    menu_archivo.add_command(label='abrir')
    menu_archivo.add_command(label='guardar como..')

    #creamos menu opciones en la barra
    menu_opciones = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label =f"{menu_opciones_label}", menu = menu_opciones)

    menu_opciones.add_command(label='texto..')
    menu_opciones.add_command(label='modo oscuro')
    menu_opciones.add_command(label='modo claro')

      #creamos menu ayuda en la barra
    menu_ayuda = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label =f"{menu_ayuda_label}", menu = menu_ayuda)

    menu_ayuda.add_command(label='comandos de teclado')
    menu_ayuda.add_command(label='quienes somos')
    



