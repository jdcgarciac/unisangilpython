# Algoritmo de divide y conquista
# Primero divide una lista en partes iguales, hasta que queden sublistas de 0 o 1 elemestos.
# Luego se re combina de forma ordenada

import random

def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        #Partir la lista entre 2, division entrea
        medio = len(lista) // 2
        #Sublista 1 
        # De 0 hasta la mitad
        izquierda = lista[:medio]
        # De la mitad hasta el final
        derecha = lista[medio:]
        
        #Separacion de listas - parte izq y der
        print(izquierda, '*' * 5, derecha)

        # llamada recursiva en cada mitad
        # Para subdividir en listas, hasta conseguir listas de un solo tamaño
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        # Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        # Iterador para la lista principal
        k = 0
        
        #Generar comparaciones entre listas 
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                #Re construye la lista
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1

            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k +=1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        
        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        #Terminacion de paso
        print('-' * 50)

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
    lista_ordenada = ordenamiento_por_mezcla(lista)
    #Imprime el resultado
    print(lista_ordenada)