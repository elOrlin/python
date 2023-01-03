#condicionales


#ejemplo 1
print("#################### EJEMPLO 1 #######################")

color = input("Adivina cula es mi color favorito: ")

if color == "rojo":
    print("Enhorabuena")
    print("El color es rojo")
    
else:
    print("Color incorrecto")
    
    
    
#ejemplo 2
    print("#################### EJEMPLO 2 #######################")

year = 2022
year = int(input("En que year estamos ?"))

if year >= 2023:
    print("Estamos del 2022 en adelante")
    
else:
    print("Es un year anterior a 2024")
    
    
    #ejemplo 3
    print("#################### EJEMPLO 3 #######################")
    
    nombre = "Orlin"
    ciudad = "Puerto plata"
    continente = "latinoamericano"
    edad = 55
    mayoria_edad = 18
    
    if edad >= mayoria_edad:
        print(f"{nombre} es mayor de edad")
        
        if continente != "latinoamericano":
            print("El usaurio no es latinoamericano")
           
        else:
            print(f"es latinoamericano y de {ciudad}") 
            
    else:
        print(f"{nombre} no es mayor de edad")