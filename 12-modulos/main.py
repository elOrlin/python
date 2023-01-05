
#import modulo
#from modulo import getNombre
from modulo import *

#print(modulo.getNombre('Orlin Diaz'))
print(getNombre('Orlin De Los Santos'))
print(getApellido("Diaz Diaz"))


#modulo fechas
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()
fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")

print(fecha_completa)
print(f"{fecha_completa.hour}:{fecha_completa.minute}")

print(f"fecha personalizada {fecha_personalizada}")

#Modulo matematicas
import math

print('Raiz cuadrada de 10:', math.sqrt(10))
print('Numero pi:', float(math.pi))
print('Redondear', math.ceil(6.56789))
print('Redondear', math.floor(6.56789))

#Modulo random
import random

print("Numero aleatorio entre 15 y 67:", random.randint(15, 67))