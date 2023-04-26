#funcion menu
def menu():
    """
    Muestra el menu al usuario y devuelve la opcion digitada en formato int
    """
    print("\n Calculadora de figuras geometricas")
    print("1. Calcular area del cuadrado")
    print("2. Calcular area del circulo")
    print("3. Calcular area del triangulo")
    print("4. Salir")
    op = int(input("Digite la opción: "))
    return op

#funcion solicitar datos
def datos_cuadrado():
    """
    Solicitar el lado del cuadrado y lo transforma y retorna float
    """
    lado = float(input("Digite el lado: "))
    return lado

#funcion solicitar datos
def datos_circulo():
    """
    Solicitar el radio del circulo y lo transforma y retorna float
    """
    radio = float(input("Digite el radio: "))
    return radio

#funcion solicitar datos
def datos_triangulo():
    """
    Solicitar base y altura del triangulo y lo transforma y retorna float base y altura
    """
    base = float(input("Digite la base: "))
    altura = float(input("Digite la altura: "))
    return base,altura

#Funcion mostrar datos
def mostrar_cuadrado(area):
    """
    Muestra el area del cuadrado al usuario final
    """
    print(f"El area del cuadrado es {area} mts^2")

def mostrar_circulo(area):
    """
    Muestra el area del circulo al usuario final
    """
    print(f"El area del circulo es {area} mts^2")

def mostrar_triangulo(area):
    """
    Muestra el area del triangulo al usuario final
    """
    print(f"El area del triangulo es {area} mts^2")