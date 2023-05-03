#Libreria
import json
#Creas diccionario
diccionario={}
#Diccionario con datos
unisangil = {
  "nombre":"Jesús David García Caro",
  "correo":"jdgarcia1@unisangil.edu.co",
  "deportes":[
      "futbol","natacion", "tejo"
    ],
  "estudiantes":[
     {"estudiante1":
    {
        "nombre":"David Contreras",
        "codigo":13234
    }
     },

    {"estudiante2": {
        "nombre":"Camila Avila",
        "codigo":1345456
    }
    }
 ]
}
#Ver informcion
#print(unisangil)
#Accerder info especifica
#print(unisangil["nombre"])
#print(unisangil["correo"])
#print(unisangil["deportes"])
"""
for x in unisangil["deportes"]:
    print(x)


for estudiante in unisangil["estudiantes"]:
    print(estudiante)

#items
print(unisangil.items())

#Valores
print(unisangil.values())

#llaves
print(unisangil.keys())

#imprimir varios valores clave valor
for keys,values in unisangil.items():
    print(f"{keys}: {values}")
"""
x = unisangil["estudiantes"]
print(x)

for estudiante in x:
    print(estudiante.keys())
    for keys,values in estudiante.items():
     print(f"{keys}: {values}")
     