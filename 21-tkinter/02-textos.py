from tkinter import *

ventana = Tk()

ventana.geometry("500x500")

texto = Label(ventana, text="Bienvenido a mi clase de texto")
texto.config(
    height=3,
    bg="orange",
    font=("Arial", 18)
)

texto.pack(anchor=CENTER)

ventana.mainloop()