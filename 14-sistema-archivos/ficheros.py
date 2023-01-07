#Abrir ficheros
from io import open
import pathlib

ruta = str(pathlib.Path().absolute()) + "/ficheros_texto.txt"

archivo = open(ruta, "a+")

#escribir en un archivo
archivo.write("************** SOY UN TEXTO DENTRO DE PYTHON ****************\n")
print(archivo)
#cerrar archivos
archivo.close()

#leer contenido
ruta = str(pathlib.Path().absolute()) + "/14-sistema-archivos/ficheros_texto.txt"
archivo_lectura = open(ruta, "r")

contenido = archivo_lectura.read()
for elemento in contenido:
    print(f"este es el {elemento}")
    
#leer contenido y guardar lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

for frase in lista:
    frase_lista = frase.split()
    print(frase.center(100))
    
    #copiar archivo
    ruta_original = str(pathlib.Path().absolute()) + "/14-sistema-archivos/ficheros_texto.txt"
    ruta_nueva = str(pathlib.Path().absolute()) + "/14-sistema-archivos/ficheros_copiado.txt"
    shutil.copyfile(ruta_original, ruta_nueva)