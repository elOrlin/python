class Coche:
    color = 'rojo'
    marca = 'ferrari'
    modelo = 'aventador'
    velocidad = 300
    caballaje = 500
    plazas = 2
    
    #constructor
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas
    
    #crear getters y setters
    
    #agregando color
    def setColor(self, color):
        self.color = color
        
   # devolviendo resutaldo del color
    def getColor(self):
        return self.color
    
    def setMarca(self, marca):
        self.marca = marca
        
    def getMarca(self):
        return self.marca
    
    def setModelo(self, modelo):
        self.modelo = modelo
        
    def getModelo(self):
        return self.modelo
    
    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1
        
    def getVelocidad(self):
        return self.velocidad
    
    def getInfo(self):
        
        info = "----- Informacion del coche -----"
        info += f'\n Color: {self.getColor()}'
        info += f'\n Marca: {self.getMarca()}'
        info += f'\n Modelo: {self.getModelo()}'
        info += f'\n Velocidad: {str(self.getVelocidad())}'
        
        return info