#Definición de conjuntos
A = {1,2,3,4,5,6}
B = {5,6,7,8}
C = {6,7,8,9,10}

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