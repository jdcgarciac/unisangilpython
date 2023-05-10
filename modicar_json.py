#Libreria
import json
from datetime import datetime
#Ruta
ruta = "data/unisangil.json"
#escribir
archivo = open(ruta, "r")
#leer json
contenido = json.load(archivo)
print(contenido)
#Cerrar archivo
archivo.close()
#Modificar informacion 
correo = input("Digite el correo a modificar: ")
celular = int(input("Digite el numero del celular: "))
materia = input("Digite la materia a agregar: ")
#Informacion 
contenido["correo"] = correo
contenido["celular"] = celular
contenido["materia"] = materia
#del contenido["celualr"]
contenido["Fecha-Hora"] = str(datetime.now())

#escribir
archivo = open(ruta, "w")
#Guardar json
json.dump(contenido,archivo)
#Cerrar archivo
archivo.close()

#Leer nuevamente
#escribir
archivo = open(ruta, "r")
#leer json
contenido = json.load(archivo)
print(contenido)
#Cerrar archivo
archivo.close()