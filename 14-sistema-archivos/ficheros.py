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
    
#mover archivos
ruta_copiado = str(pathlib.Path().absolute()) + "/14-sistema-archivos/ficheros_copiado.txt"
ruta_copiado_nueva = str(pathlib.Path().absolute()) + "/14-sistema-archivos/ficheros_copiado_NUEVA.txt"

shutil.move(ruta_copiado, ruta_copiado_nueva)
    
#eliminar archivos
#para eliminar archivos necesitamos importar otro metodo llamado (OS)
import os

os.remove(ruta_copiado_nueva)

#comprobar si un archivo existe
import os.path

print(os.path.abspath("../"))
ruta_comprobar = os.path.abspath('./') + "/ficheros_texto.txt"

print(ruta_comprobar)

if os.path.isfile(ruta_comprobar):
    print("el archivo existe")
else:
    print('el archivo no existe')
    