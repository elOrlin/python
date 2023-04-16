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

class Nota:
    def __init__(self, usuario_id, titulo, descripcion):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
        
    def guardar(self):
        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW())"
        nota = (self.usuario_id, self.titulo, self.descripcion)
        
        cursor.execute(sql, nota)
        database.commit()
        
        return [cursor.rowcount, self]