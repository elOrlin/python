#ejemplo 5
print("\n#################### EJEMPLO 5 #######################")

edad__minima = 18
edad__maxima = 65
edad__oficial = int(input("Tienes edad de trabajar> introduce tu edad"))

if edad__oficial >= 18 and edad__oficial <= 65:
    print("Esta en edad de trabajar")
else:
    print("No esta en edad de trabajar")
    
    
    #ejemplo 6
    print("\n#################### EJEMPLO 6 #######################")

    pais = "Alemania"

    if pais == 'Mexico' or pais == 'Espana' or pais == 'Colombia':
        print(f"{pais} Es un pais de habla hispana")
    else:
        print(f"{pais} no es un pais de habla hispana")