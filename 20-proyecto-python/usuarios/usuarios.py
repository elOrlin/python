 #usuarios
import mysql.connector
import hashlib
 
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
        fecha = datetime.datetime.now()
        
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)
        
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
            
        return result
        
    def identificar(self):
        
        #Consulta para comprobar si existe el usuario
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        
        #Cifrar contrasena
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode("utf8"))
        
        #Datos para la consulta
        usuario = (self. email, cifrado.hexdigest())
        
        cursor.execute(sql, usuario)
        result = cursor.fetchone()
        
        return result
    