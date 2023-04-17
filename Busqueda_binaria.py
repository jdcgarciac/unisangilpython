# Estrategia de divide y conquista
# El problema se divide en 2 en cada iteración
# Asume que la lista este ordenada, se debe ordenar primero

# Libreria de numeros aleatorio
import random

def busqueda_binaria(lista, comienzo, final, objetivo):
    #Si se viene de un indice se tiene que restar un 1
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    if comienzo > final:
        #Si el comienzo es mas grande que el final, ya no lo encontramos
        return False
    # Dividir la lista en 2, utiliza division de enteros (No importa la parte decimal)
    # Encuentra la mitad de donde nos encontramos en la lista
    medio = (comienzo + final) // 2
    # Se compara si ya encontramos el objetivo
    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        #Recorrer parte de arriba, se desplaza el comienzo 
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        #Recorrer parte de abajo, se desplaza el final
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)

# Que si este archivo se ejecuta directamente desde la consola
if __name__ == '__main__':
    # Pregunta y transforma a int
    tamano_de_lista = int(input('De que tamano es la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))
    # Crea una lista de manera aleatoria de numeros de 0 a 100 del tamaño de la lista
    # Ordena la lista
    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])
    #Llama la funcion y le pasa los parametros(Lista y Objetivo) y la almacena en la variable
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    #Impresion de informacion
    print(lista)
    #Operador termiario en una sola linea de codigo
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')

    