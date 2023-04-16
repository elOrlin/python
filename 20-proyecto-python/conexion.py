import mysql.connector

## Conexión
def conectar():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        port=3306,
        passwd="root",
        database="master_python"
    )

    cursor = database.cursor(buffered=True)
    return [database, cursor]