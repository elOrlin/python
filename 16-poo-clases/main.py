#Programacion orientada a objectos (POO o OOP)

class Coche:
    color = 'rojo'
    marca = 'ferrari'
    modelo = 'aventador'
    velocidad = 300
    caballaje = 500
    plazas = 2
    
    #crear getters y setters
    
    #agregando color
    def setColor(self, color):
        self.color = color
    
    #devolviendo resutaldo del color
    def getColor(self):
        return self.color
    
    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1
        
    def getVelocidad(self):
        return self.velocidad
     
auto = Coche()

print(auto.marca)
print(f'Velocidad actual: {auto.velocidad}')

auto.setColor('perla')
auto.acelerar()
auto.frenar()
print(auto.color)
print(f'Velocidad nueva: {auto.velocidad}')