#aprendiendo sobre funciones

def nombreUsuarios(nombre, edad):
    print(f'tu nombre es {nombre}')
    
    if edad >= 18:
        print('eres mayor de edad')
    
nombre = input('Introduce tu nombre:')
edad = int(input('Introduce tu edad:'))
nombreUsuarios(nombre, edad)


def tabla(numero):
    print(f"tabla de multiplicar del numero: {numero}")
    
    for contador in range(13):
        operacion = numero*contador
        print(f"{numero} X {contador} = {operacion}")
        
        print("\n")
        
tabla(7)


#parametros opcionales
def getEmpleados(nombre, dni = None):
    print("EMPLEADO")
    print(f"nombre: {nombre}")
    
    if dni != None:
        print(f"DNI: {dni}")
    
getEmpleados('Orlin', 123456789)

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"
    
    return saludo
print(saludame('Orlin Diaz'))

def calculadora(numero1, numero2, basicas = False):
    
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    divicion = numero1 / numero2
    
    cadena = ""
    
    if basicas != False:
        cadena += f"suma: {str(suma)}"
        cadena = "\n"
        cadena += f"resta: {str(resta)}"
        cadena = "\n"
    
    else:
        cadena += f"multi: {str(multi)}"
        cadena = "\n"
        cadena += f"divicion: {str(divicion)}"
    
        return cadena
    
print(calculadora(50, 5, True))