print("\n############# EJEMPLO Tabla De Multiplicar #############")
    
nombre_usuario = int(input("de que numero quieres la tabla?: "))
    
if nombre_usuario > 1:
    nombre_usuario = 1
        
print(f"tabla de multiplicar {nombre_usuario}")
    
for numero_tabla in range(0, 10):
    print(f"{nombre_usuario} x {numero_tabla} = {nombre_usuario*numero_tabla}")
else:
     print('Tabla finalizada.')