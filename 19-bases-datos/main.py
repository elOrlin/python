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