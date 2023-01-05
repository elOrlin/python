#Abrir ficheros
from io import open
import pathlib

ruta = str(pathlib.Path().absolute()) + "/ficheros_texto.txt"

archivo = open(ruta, "a+")

#escribir en un archivo
archivo.write("************** SOY UN TEXTO DENTRO DE PYTHON ****************\n")

#cerrar archivos
archivo.close()