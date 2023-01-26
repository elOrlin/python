from tkinter import *
import os.path

ventana = Tk()

ventana.geometry("500x500")
ventana.title("Programacion orientada a objectos en python")

#botones check
def mostrarProfesion():
    texto = ""
    if web.get():
        if movil.get():
            texto += "Desarrollo Web "
        else:
            texto += "y Desarrollo Movil"
        
    if movil.get():
        if web.get():
            texto += "y Desarrollo Movil"
        else:
            texto += "Desarrollo Movil"
            
    mostrar.config(text=texto, bg="green", fg="white")
    
web = IntVar()
movil = IntVar()

Label(ventana, text="Aque te dedicas? ").grid(row=0, column=0)
Checkbutton(ventana, text="Desarrollo Web", variable=web, onvalue=1, offvalue=0, command=mostrarProfesion).grid(row=1, column=0)
Checkbutton(ventana, text="Desarrollo Movil", variable=movil, onvalue=1, offvalue=0, command=mostrarProfesion).grid(row=2, column=0)

mostrar = Label(ventana)
mostrar.grid(row=3, column=0)