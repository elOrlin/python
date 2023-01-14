#cargar imagnes con pillow
from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()

ventana.geometry("700x500")

texto = Label(ventana, text="Bienvenido a mi clase")
texto.pack(anchor=W)

imagen = Image.open("21-tkinter\imagenes\python.png")
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack()

ventana.mainloop()