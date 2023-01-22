from tkinter import *
from tkinter import messagebox

ventana = Tk()

ventana.geometry("300x300")

ventana.title("Ejercicios completo con tkinter | Orlin Diaz")
ventana.config(
    bd=25
)

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

Label(ventana, text="Primer Numero: ").pack()
Entry(ventana, textvariable=numero1).pack()

Label(ventana, text="Segundo Numero: ").pack()
Entry(ventana, textvariable=numero2).pack()

Label(ventana, text="").pack()

Button(ventana, text="Sumar").pack(side="left")
Button(ventana, text="Restar").pack(side="left")
Button(ventana, text="Multiplicar").pack(side="left")
Button(ventana, text="Dividir").pack(side="left")

ventana.mainloop()