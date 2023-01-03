#condicionales


#ejemplo 1
print("\n#################### EJEMPLO 1 #######################")

color = input("Adivina cula es mi color favorito: ")

if color == "rojo":
    print("Enhorabuena")
    print("El color es rojo")
    
else:
    print("Color incorrecto")
    
    
    
#ejemplo 2
    print("\n#################### EJEMPLO 2 #######################")

year = 2022
year = int(input("En que year estamos ?"))

if year >= 2023:
    print("Estamos del 2022 en adelante")
    
else:
    print("Es un year anterior a 2024")
    
    
#ejemplo 3
    print("\n#################### EJEMPLO 3 #######################")
    
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
        
        
    #ejemplo 4
    print("\n#################### EJEMPLO 4 #######################")
    
    dia = int(input("Introduce el numero dia de la semana: "))
                        
                        
if dia == 1:
    print("Es lunes")
elif dia == 2:
   print("Es martes")
elif dia == 3:
   print("Es miercoles")
elif dia == 4:
   print("Es jueves")
elif dia == 5:
   print("Es viernes")
else:
   print("Es fin de semana") 
   
   
   
   """
        if dia == 1:
        print("Es lunes")
    else:
        if dia == 2:
            print("Es martes")
        else:
            if dia == 3:
                print("Es miercoles")
            else:
                if dia == 4:
                    print("Es jueves")
                else:
                    if dia == 5:
                        print("Es viernes")
                    else:
                        print("Es fin de semana")
   """