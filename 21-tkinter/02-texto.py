from tkinter import *

ventana = Tk()

ventana.geometry("500x500")

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
texto.pack(anchor=SE)

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
texto.pack(anchor=NW)

ventana.mainloop()