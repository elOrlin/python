#detectar el tipado de una variable

nombre = 'Orlin Diaz'

print(type(nombre))

comprobar = isinstance(nombre, str)
if comprobar:
    print("esa viriable es un string")
else:
    print("esa variable no es una cadena")
    
    

################### Funciones con variables definidas fuera de la funcion ###########################

def mi_funcion(): 
    return f"Hola que tal {nombre}"

def mi_segunda_funcion(): 
    return f"Hola que tal {apellidos}"

nombre = 'Orlin'
apellidos = 'Diaz Diaz'

print(mi_funcion())
print(mi_segunda_funcion())