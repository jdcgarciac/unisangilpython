#py -m pip install mysql-connector-python
#Libreria
import mysql.connector
import pandas as pd
#Leer el excel
ruta = "Base de datos/Iris.csv"
df = pd.read_csv(ruta)
#Imprimir datos
print(df.head())
#Establecer conexion con la base de datos
conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "iris",
    port = 3306
)
#Crear un cursor para generar consultas
cursor = conexion.cursor()
#Insertar datos
for index,row in df.head(150).iterrows():
    #Generar consultas en sql
    sql = "INSERT INTO datos (Id,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm,Species) VALUES(%s,%s,%s,%s,%s,%s)"
    datos = (row["Id"],row["SepalLengthCm"],row["SepalWidthCm"],row["PetalLengthCm"],row["PetalWidthCm"],row["Species"])
    #Comando
    cursor.execute(sql,datos)
#Commit
conexion.commit()
#Cerrar el cursor y la conecxion a bd
cursor.close()
conexion.close()