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

#eliminar productos
#curosr.Execute("DELETE FROM productos")

#insertar productos de un golpe
productos = [
    ('Ordenador portatil', 'Buen PC', 700),
    ('Telefono Movil', 'Buen Telefono', 140),
    ('Placa base', 'Buena Placa', 80),
    ('Tablet 15', 'Buena Tablet', 300)
]

cursor.executemany("INSERT INTO PRODUCTOS VALUES (null,?,?,? )", productos)
conexion.commit()

#UPDATE
cursor.execute("UPDATE productos SET precio=678 WHERE precio=80")

#leer datos (listar datos)
cursor.execute("SELECT * FROM productos WHERE precio >= 300;")
productos = cursor.fetchall()

for producto in productos:
    print(f'ID: {producto[0]}')
    print(f'Titulo: {producto[1]}')
    print(f'Descripcion: {producto[2]}')
    print(f'Precio: {producto[3]}')
    print('\n')
    
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()
print(producto)

#cerrar conexion
conexion.close()