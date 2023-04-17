#simplemente modifican los valores en memoria.
#Una lista es dividida entre una sublista ordenada y otra sublista desordenada.
#La inserción se realiza al mover todos los elementos mayores al elemento que se está evaluando un lugar a la derecha.
#No sirve para una gran cantidad de datos

# Libreria de numeros aleatorio
import random

#Funcion
def ordenamiento_por_insercion(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual

# Que si este archivo se ejecuta directamente desde la consola
if __name__ == '__main__':
    # Pregunta y transforma a int
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    # Crea una lista de manera aleatoria de numeros de 0 a 100 del tamaño de la lista
    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    #Imprime la lista
    print(lista)
    #Llama la funcion y le pasa el parametro(Lista) y la almacena en la variable
    lista_ordenada = ordenamiento_por_insercion(lista)
    #Imprime el resultado
    print(lista_ordenada)