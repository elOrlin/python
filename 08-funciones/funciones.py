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

#funciones lambdas
dime_el_year = lambda year: f"El year es {year}"

print(dime_el_year(2034))