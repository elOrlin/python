from tkinter import *
from tkinter import messagebox

ventana = Tk()

ventana.geometry("300x300")

ventana.title("Calculadora | Orlin Diaz")
ventana.config(
    bd=25
)

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco = Frame(ventana, width=250, height=250)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID
)

def convertirFloat(numero):
    try:
        result = float(numero)
    except:
        result = 0
        messagebox.showerror("Error", "Introduce bien los datos")
    return result

def sumar():
    resultado.set(convertirFloat(numero1.get()) + convertirFloat(numero2.get()))
    mostrarResultado()
    
def restar():
    resultado.set(convertirFloat(numero1.get()) - convertirFloat(numero2.get()))
    mostrarResultado()
    
def multiplicar():
    resultado.set(convertirFloat(numero1.get()) * convertirFloat(numero2.get()))
    mostrarResultado()
    
def dividir():
    resultado.set(convertirFloat(numero1.get()) / convertirFloat(numero2.get()))
    mostrarResultado()
    
def mostrarResultado():
    messagebox.showinfo("Resultado", f"El resultado de la operacion es: {resultado.get()}")
        
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Primer Numero: ").pack()
Entry(marco, textvariable=numero1, justify="center").pack()

Label(marco, text="Segundo Numero: ").pack()
Entry(marco, textvariable=numero2, justify="center").pack()

Label(marco, text="").pack()

Button(marco, text="Sumar", command=sumar).pack(anchor=CENTER, fill=X, expand="YES")
Button(marco, text="Restar", command=restar).pack(anchor=CENTER, fill=X, expand="YES")
Button(marco, text="Multiplicar", command=multiplicar).pack(anchor=CENTER, fill=X, expand="YES")
Button(marco, text="Dividir", command=dividir).pack(anchor=CENTER, fill=X, expand="YES")

ventana.mainloop()