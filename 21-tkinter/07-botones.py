from tkinter import *

ventana = Tk()

ventana.geometry("500x500")

boton = Button(ventana, text="Enviar")

boton.grid(row=5, column=1, sticky=W)

boton.config(padx=15, pady=15, bg="green", fg="white")

ventana.mainloop()