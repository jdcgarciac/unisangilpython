#Libreria
import json
#Diccionario con datos
unisangil = {
  "nombre":"Jesus David Garcia Caro",
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
#imprimir 
print(unisangil)
#escribir
archivo = open("unisangil.json", "w")
#Guardar json
json.dump(unisangil,archivo)
#Cerrar archivo
archivo.close()