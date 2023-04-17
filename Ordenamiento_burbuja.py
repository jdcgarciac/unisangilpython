# Libreria de numeros aleatorio
import random

#Funcion
def ordenamiento_de_burbuja(lista):
    # Obtener el tamaño de la lista
    n = len(lista)
    
    #Recorremos el tamaño de la lista
    for i in range(n):
        # Recorre la lista varias veces (Tamaño de la lista, TL - i(Lo que ya recorrimos) - 1 (Posicion, por utilizar indices))
        # Recorre cada vez menor al tamaño de la lista
        for j in range(0, n - i - 1):
            #Regla para orgenamiento
            # Comparar indices de la lista
            if lista[j] > lista[j + 1]:
                # Intercambia valores de la lista y reasigna
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    #Retorna Lista ordenada
    return lista

# Que si este archivo se ejecuta directamente desde la consola
if __name__ == '__main__':
    # Pregunta y transforma a int
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    # Crea una lista de manera aleatoria de numeros de 0 a 100 del tamaño de la lista
    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    #Imprime la lista
    print(lista)
    #Llama la funcion y le pasa el parametro(Lista) y la almacena en la variable
    lista_ordenada = ordenamiento_de_burbuja(lista)
    #Imprime el resultado
    print(lista_ordenada)