numero_usuario = 0
 
print("##################EJEMPLO DE TABLA##########################")

numero_usuario = 0
numero_usuario = int(input("de que numero quieres la tabla?:"))

if numero_usuario < 1:
    numero_usuario = 1
    
    print(f"Tabla de multiplicar {numero_usuario}")
    
for numero_tabla in range(1, 13):
    
    if numero_usuario == 45:
        print("no se puede mostrar numeros prohibidos")
        
        break
        
    print(f"{numero_usuario} X {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("Tabla finalizada.")