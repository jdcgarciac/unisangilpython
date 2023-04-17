#Busca todos los elementos de manera secuencial
#Permite validar si un objeto esta o no destro de una lista

# Libreria de numeros aleatorio
import random

#Funcion con parametros (Lista y elemento a buscar)
def busqueda_lineal(lista, objetivo):
    #Bandera
    match = False
    # Recorre la lista y utiliza la variable de control
    for elemento in lista: 
        # Imprime cada iteracion
        print(f'buscando {elemento} entre {lista}')
        #Compara si el elemento de la lista es = al objetivo
        if elemento == objetivo:
            #Si es igual retorna el valor de Match en True
            match = True
            #Rompe el ciclo
            break
    # Retorna la bandera
    return match

# Que si este archivo se ejecuta directamente desde la consola
if __name__ == '__main__':
    # Pregunta y transforma a int
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))
    # Crea una lista de manera aleatoria de numeros de 0 a 100 del tamaño de la lista
    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    #Llama la funcion y le pasa los parametros(Lista y Objetivo) y la almacena en la variable
    encontrado = busqueda_lineal(lista, objetivo)
    #Impresion de informacion
    print(lista)
    #Operador termiario en una sola linea de codigo
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')