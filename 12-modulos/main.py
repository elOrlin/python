
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