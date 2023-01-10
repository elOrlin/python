from coche import Coche

carro = Coche('amarillo', 'reanult', 'bmw', 150, 200, 4)
carro1 = Coche('verde', 'seat', 'panda', 240, 200, 4)
carro2 = Coche('azul', 'citroen', 'xara', 100, 180, 4)
carro3 = Coche('rojo', 'mercedes', 'clase a', 350, 400, 4)

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

#detectar tipado
carro3 ='Aleatorio'
if type(carro3) == Coche:
    print('Es un abjeto correcto')
else:
    print('No es objeto')