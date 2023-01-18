#Modulo para crear interfaces de usuario
from tkinter import *
import os.path

class Programa:
    def __init__(self):
        self.title = "Interfaz grafica con Orlin Diaz"
        self.icon = "./imagenes/python.ico"
        self.icon_alt = "./21-tkinter/imagenes/python.ico"
        self.size = "770x450"
        self.resizable = False
        
 
    def cargar(self): 
        #crear la ventana
        ventana = Tk()
        self.ventana = ventana
        #Titulo de la ventana
        ventana.title(self.title)

        #comprobar si existe una ruta
        ruta_icon = os.path.abspath(self.icon)
        
        if not os.path.isfile(ruta_icon):
            ruta_icon = os.path.abspath(self.icon_alt)
            
        ventana.iconbitmap(ruta_icon)
        texto = Label(ventana, text=ruta_icon)
        texto.pack()

        #cambio en el tamano de la ventana
        ventana.geometry(self.size)
        
        #bloquear el tamano de la ventana
        if self.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0, 0)
        
    def addTexto(self, dato):
        texto = Label(self.ventana, text=dato)
        texto.pack() 
        
    def mostrar(self):
        #arrancar y mostrar la ventana hasta que cierre
        self.ventana.mainloop()
        
#instanciar mi programa
programa = Programa()
programa.cargar()
programa.addTexto("Hola desde un metodo")
programa.mostrar()