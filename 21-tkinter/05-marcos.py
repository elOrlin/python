from tkinter import *
import os.path

ventana = Tk()

ventana.title('Marcos | Master en Python')

ventana.geometry("700x700")

ruta = os.path.abspath("./imagenes/python.ico")

if not os.path.isfile(ruta):
    ruta = os.path.abspath("./21-tkinter/imagenes/python.ico")
    ventana.iconbitmap(ruta)
    texto = Label(ventana, text=ruta)
    texto.pack()

marco = Frame(ventana, width=250, height=250)
marco.config(
    bg="red",
    bd=5,
    relief=SOLID
)

marco.pack(side=LEFT, anchor=SW)
marco.pack_propagate(False)

texto = Label(marco, text="Primer marco")
texto.config(
    bg="red",
    fg="white",
    font=("Arial", 20),
    height=10,
    anchor=CENTER,
    width=10
)
texto.pack()

marco = Frame(ventana, width=250, height=250)
marco.config(
    bg="green",
    bd=5,
    relief=SOLID
)

marco.pack(side=RIGHT, anchor=SE)

marco = Frame(ventana, width=250, height=250)
marco.config(
    bg="blue",
    bd=5,
    relief=SOLID
)

marco.pack(side=TOP, fill=X, anchor=N, expand=YES)

ventana.mainloop()