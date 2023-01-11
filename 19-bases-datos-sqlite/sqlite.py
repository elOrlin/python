#importar el modulo
import sqlite3

#conexion
conexion = sqlite3.connect('pruebas.db')

#crear cursor
cursor = conexion.cursor()

#crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
    "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"+
   "titulo VARCHAR(255),"+
   "descripcion TEXT,"+
   "precio int(255)"+
")")

#guardar cambios
conexion.commit()

#insertar datos
cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'Descriptcion de mi producto', 550)")
conexion.commit()

curosr.Execute("DELETE FROM productos")

#leer datos (listar datos)
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()

for producto in productos:
    print(f'titulo: {producto[1]}')
    print(f'descripcion: {producto[2]}')
    print(f'usuarios: {producto[3]}')
    print('\n')

#cerrar conexion
conexion.close()