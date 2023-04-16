from tkinter import *

ventana = Tk()

ventana.geometry("500x500")

ventana.config(
    bd=50,
    bg="#ccc"
)

def getDatos():
    resultado.set(datos.get())
    
    if len(resultado.get()) >= 1:
        texto_recogido.config (
            bg="green",
            fg="white"
        )
    
datos = StringVar()
resultado = StringVar()

Label(ventana, text="Agrega un texto").pack(anchor=NW)
Entry(ventana, textvariable=datos).pack(anchor=NW)

Label(ventana, text="Datos recogidos: ").pack(anchor=NW)
texto_recogido = Label(ventana, textvariable=resultado)

texto_recogido.pack(anchor=NW)

Button(ventana, text="Mostrar datos", command=getDatos).pack(anchor=NW)

ventana.mainloop()