"""
#Llibreria
import random
#Definición de conjuntos
# Generar un conjunto aleatorio de 10 números enteros del 1 al 100
A = set(random.sample(range(1, 101), 10))
B = set(random.sample(range(1, 101), 10))
C = set(random.sample(range(1, 101), 10))
#Datos
print(f"Conjunto A: {A}")
print(f"Conjunto B: {B}")
print(f"Conjunto C: {C}")

#Operación 1
R = B.intersection(C)
print(R)

#Operación 1
R = A.intersection(B)
print(R)
#Operación 2
Z = R.intersection(C)
print(Z)
#Ooperacion 3
RT = Z.union(B) ## Z|B
print(RT)
# | -----> Union
# & -----> iINTERSECCION
RT1 = ((A & B)& C)| B
print(RT1)

#Ejercicio 1
A = {1,2,3,4,5}
B = {4,5,6}
C = {5,6,7,8,9,10}
D = {10,11,12}

RT = A.difference(B)
print(RT)

RT1 = (((A-B)|(C-B)) & (C-B)) & (B-C)
print(RT1)
"""
#Subconjunto
A = {1,2,3,4,5}
B = {3,4,5}

S = (A <= B)
print(S)

if S:
    RT = A & B
    print(RT)
else:
    print("Conjunto Vacio")


