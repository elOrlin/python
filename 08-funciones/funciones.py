def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"El nombre es: {apellidos}"
    return texto

def devuelveTodo(nombre, apellidos):
    texto = f"{getNombre(nombre)} {getApellidos(apellidos)}"
    return texto

print(devuelveTodo('Orlin', 'Diaz'))

