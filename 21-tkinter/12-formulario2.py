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

def marcar():
    marcado.config(text=opcion.get())

opcion = StringVar()
opcion.set(None)

marcado = Label(ventana)
marcado.grid(row=7)

Label(ventana, text="Cual es tu genero? ").grid(row=4)
Radiobutton(ventana, text="Masculino", value="Masculino", variable=opcion, command=marcar).grid(row=5)
Radiobutton(ventana, text="Femenino", value="Femenino", variable=opcion, command=marcar).grid(row=6)

def selecionar():
    selecionado.config(text=select.get())

select = StringVar()
select.set("Opcion 1")

Label(ventana, text="Selecciona una opcion? ").grid(row=4, column=1)

selecto = OptionMenu(ventana, select, "Opcion 1", "Opcion 2", "Opcion 3" )
selecto.grid(row=5, column=1)

boton = Button(ventana, text="Ver", command=selecionar)
boton.grid(row=6, column=1)

selecionado = Label(ventana)
selecionado.grid(row=7, column=1)

ventana.mainloop()