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