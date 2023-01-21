from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()

ventana.geometry("500x500")
ventana.config(bd=70)

def mostrarAlerta():
    MessageBox.showerror("Alerta", "Mostrar Alerta")
    
Button(ventana, text="Mostrar Alerta", command=mostrarAlerta).pack()
    
def salir(nombre):
   resultado = MessageBox.askquestion("Salir", "Deseas continuar ejecutando la aplicacion ? ")
   if resultado != "yes":
        MessageBox.showinfo("Chao", f"adios {nombre}")
        ventana.destroy()

Button(ventana, text="Salir", command=lambda: salir("Orlin Diaz")).pack()

ventana.mainloop()