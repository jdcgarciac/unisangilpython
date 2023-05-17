#py -m pip install mysql-connector-python
#Libreria
import mysql.connector
#Establecer conexion con la base de datos
conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "seguidor_linea",
    port = 3306
)
#Crear un cursor para generar consultas
cursor = conexion.cursor()
#Generar consultas en sql
sql = "SELECT * FROM datos"
#Comando
cursor.execute(sql)
#Almacernar los datos
sensores = cursor.fetchall()
#Recorrer los resultadoe e imprimirlos
for datos in sensores:
    print(f"Datos seguidor: {datos}")
#Cerrar el cursor y la conecxion a bd
cursor.close()
conexion.close()

