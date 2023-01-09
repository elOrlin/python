import os, shutil

if not os.path.isdir('./mi_carpeta'):
    os.mkdir('./mi_carpeta')
else:
    print('Ya existe el directorio')
    
#copiar carpetas
ruta_original = './mi_carpeta'
ruta_copiada = './mi_carpeta_COPIADA'

shutil.copytree(ruta_original, ruta_copiada)

os.rmdir('./mi_carpeta_COPIADA')

print('contenido de mi carpeta')
contenido = os.listdir('./mi_carpeta')
    
for fichero in contenido:
    print('Fichero: ' + fichero)