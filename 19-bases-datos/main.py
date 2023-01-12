import mysql.connector
 
## Conexión
database = mysql.connector.connect(
    host="localhost",
    user="root",
    port=3306,
    passwd="root",
    database="master_python"
)

#La conexion ha sido correcta
print(database)

cursor = database.cursor()

cursor.execute("CREATE DATABASE master_python")

cursor.execute("SHOW DATABASE")

cursor.execute(""" 
CREATE TABLE IF NOT vehiculos(
    id int(10) auto_increment not null,
    marca varchar(10) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)           
""")

#cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)
database.commit()
     
#si quiero sacar toda la informacion de mi base datos usar (SELECT)
cursor.execute("SELECT * FROM vehiculos WHERE precio >= 5000 AND marca = 'Renault' ")
#sacar todos los datos que tengo
result = cursor.fetchall()

for coche in result:
    print(coche[1], coche[2], coche[3])
        
    
    cursor.execute("SELECT * FROM vehiculos")
    coche = cursor.fetchone()
    print(coche)
    
    #borrar 
    cursor.execute("DELETE FROM vehiculos WHERE marca = 'Mercedes'")
    database.commit()
    
    #mostrar los elementos borrados 
    print(cursor.rowcount, 'borrados!!')
    
    #actualizar
    cursor.execute("UPDATE vehiculos SET marca='Renault' WHERE modelo='Clio'")
    database.commit()
    
    print(cursor.rowcount, 'actualizados!!')