"""
#Estructura
for control in range(0,10,2):
    print(control)
#Listas
lista = [1,2,3,True,"unisangil",3.44]
tupla = (1,2,34,5)
print(lista[3])
print(lista[:])
print(lista[3:])
print(lista[:3])
print(lista[3:5])
print(lista[1:5])
print(len(lista))
#Metodos para las listas
#Estructura
for control in lista:
    print(control)
for control in tupla:
    print(control)
#insert
lista.insert(5,"Un")
print(lista)
#append
lista.append(123)
print(lista)
#pop
lista.pop()
print(lista)
#remove
lista.remove("unisangil")
print(lista)
"""
import random

lista_aleatoria = [random.randint(1,101) for i in range(101)]
print(lista_aleatoria)