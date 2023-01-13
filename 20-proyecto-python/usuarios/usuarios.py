 #usuarios
import mysql.connector
 
## Conexión
database = mysql.connector.connect(
    host="localhost",
    user="root",
    port=3306,
    passwd="root",
    database="master_python"
)

cursor = database.cursor(buffered=True)

class Usuario:
    
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
        
    def registrar(self):
        fecha = '12/1/2023'
        sql = "INSERT INTO usuarios VALUES (null, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, self.password, fecha)
        
        cursor.execute(sql, usuario)
        database.commit()
        
        return [cursor.rowcount, self]
        
    def identificar(self):
        return  self.nombre
    