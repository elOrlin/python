from tkinter import *
import os.path

ventana = Tk()

ventana.geometry("500x500")

ventana.title('Programando con Tkinter')
 #comprobar si existe una ruta
ruta_icon = os.path.abspath("./imagenes/python.ico")
        
if not os.path.isfile(ruta_icon):
 ruta_icon = os.path.abspath("./21-tkinter/imagenes/python.ico")
            
ventana.iconbitmap(ruta_icon)
texto = Label(ventana, text=ruta_icon)
texto.pack()

texto = Label(ventana, text="Bienvenido a mi clase")
texto.config(
    fg="white",
    height=3,
    bg="green",
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="spider"
)
texto.pack(side=TOP, fill=X, expand=YES)

texto = Label(ventana, text="Spider man master")
texto.config(
    fg="red",
    height=3,
    bg="black",
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="spider"
)
texto.pack(side=TOP, fill=X, expand=YES)

ventana.mainloop()