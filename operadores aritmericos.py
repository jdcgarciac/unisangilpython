#Libreria
import math

##Adquiriri informacion 
#Entradas
a = int(input("Digite el numero 1: "))
print(f"El numero a es: {a}")
b = int(input("Digite el numero 2: "))
print(f"El numero a es: {b}")
#Proceso
c = a + b
d = a - b
e = a * b
f = a / b
g = a ** b
h = math.sqrt(a)
#Salida
print(f"El resultado de la suma es : {c}")
print(f"El resultado de la resta es : {d}")
print(f"El resultado de la multiplicación es : {e}")
print(f"El resultado de la suma división : {f}")
print(f"El resultado de la potencia : {g}")
print(f"El resultado de la raiz de a es : {h}")

#Ejercicio
R = 15/3*(7+(68-15*33+((45**2)/5)/3)/2)+19
print(R)
#Ejercicio 2
A = (4+8*2)/4-(3**2)+math.sqrt(4)
print(A)