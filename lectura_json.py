#Libreria
import json
#escribir
archivo = open("unisangil.json", "r")
#leer json
contenido = json.load(archivo)
print(contenido)
#Cerrar archivo
archivo.close()