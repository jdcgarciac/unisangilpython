from operaciones import area_cuadrado,area_circulo,area_triangulo
from interfaz import menu,datos_cuadrado,datos_circulo,datos_triangulo,mostrar_circulo,mostrar_cuadrado,mostrar_triangulo
#variables menu
CUADRADO = 1
CIRCULO = 2
TRIANGULO = 3
SALIR = 4

opcion = 0

while opcion != SALIR:
    #Opcion menu
    opcion = menu()
    if opcion == CUADRADO:
        #Llamar la funcion de solicitar datos
        lado = datos_cuadrado()
        #Llamae a area
        area = area_cuadrado(lado)
        #Llamar a mostrar datos
        mostrar_cuadrado(area)
    elif opcion == CIRCULO:
        #Llamar la funcion de solicitar datos
        radio = datos_circulo()
        #Llamae a area
        area = area_circulo(radio)
        #Llamar a mostrar datos
        mostrar_circulo(area)
    elif opcion == TRIANGULO:
        #Llamar la funcion de solicitar datos
        base,altura = datos_triangulo()
        #Llamae a area
        area = area_triangulo(base,altura)
        #Llamar a mostrar datos
        mostrar_triangulo(area)
    elif opcion == SALIR:
        print("Gracias por utilizar la calculadora de figuras geometricas!!!")       
    else:
        print("Opción Erronea!!!")
