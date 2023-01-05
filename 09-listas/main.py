#crear listas en python

peliculas = ['Batman', 'el rey de los anillos', 'terror de texas', 'the last kingdom']
cantantes = list(('arcangel', 'daddy yankee', 'don omar'))
years = list(range(2000, 2023))
variada = ['Orlin', 30, 4, 76, True, 'Otniel']

print(peliculas)
print(cantantes)
print(years)
print(variada)

#Indices 
peliculas[1] = 'Gran Torino'
print(peliculas[1])
print(peliculas[-2])
print(peliculas)

print(cantantes[0:2])


#recorrer las listas

nueva_pelicula = ""

while nueva_pelicula != 'parar':
    nueva_pelicula = input('Introduce una nueva pelicula: ')
    
    if nueva_pelicula != 'parar':
        peliculas.append(nueva_pelicula)
        
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")
    
    
    #listas multidimencionales
contactos = [
    [
        'orlin',
        'orlindiaz@outlook.com'
    ],  
    [
        'oliver',
        'oliverdiaz@outlook.com'
    ],
    [
        'olvin',
        'olvindiaz@outlook.com'
    ]
]
    
    
for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print(f"Nombre: {elemento}")
        else:
            print(f"Apellidos: {elemento}")
    print("\n")