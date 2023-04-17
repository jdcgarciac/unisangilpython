#funcion con parametros
def imprimir_nombre(nombre):
    print(f"El nombre es: {nombre}")

##Principal
imprimir_nombre("Jesus")
imprimir_nombre("Juan")
imprimir_nombre("Anderson")
imprimir_nombre("Felipe")
imprimir_nombre("Jose")

#funcion con parametros con valor de retorno
def suma(num1,num2):
    resultado = num1 + num2
    return resultado

##principal
r1 = suma(3,4)
print(r1) #7
r2 = suma(7,5)
print(r2)#12
r3 = r1 * r2
print(r3)

##Funcion on varios valores de retorno
def suma_resta(num1,num2):
    s = num1 + num2
    r = num1 - num2
    return s,r

##principal
a,b = suma_resta(8,3)
print(f"{a} y {b}")

#Funcion para solicitar datos
def capturar_datos():
    d1 = float(input("Digite el numero 1: "))
    d2 = float(input("Digite el numero 2: "))
    return d1,d2

##Principal
num1,num2 = capturar_datos()
print(f"{num1} y {num2}")
z = suma(num1,num2)
print(z)