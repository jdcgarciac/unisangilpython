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

#modificar informacion
unisangil["nombre"] = "Jesús Caro"
print(unisangil)
#Agregar
unisangil["celular"] = 3213246454
print(unisangil)

#eliminar
del unisangil["celular"]
print(unisangil)

#Crear con listas diccionarios
a = ["num1","num2","num3"]
b = [1 , 2, 3]
#zip
print(list(zip(a,b)))

new_dict = {a:b for (a,b) in zip(a,b)}
print(new_dict)


   