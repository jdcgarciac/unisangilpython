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
sql = "INSERT INTO datos (q1,q2,mensaje,fecha,hora) VALUES(%s,%s,%s,%s,%s)"
datos = 1,0,"Derecha","2023-05-17","14:33:23"
#Comando
cursor.execute(sql,datos)
#Commit
conexion.commit()
#Cerrar el cursor y la conecxion a bd
cursor.close()
conexion.close()