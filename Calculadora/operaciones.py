#Importar libreria
import math

#Funciones
def area_cuadrado(lado):
    """
    Calcula el area del cuadrado y retorna una variable
    que se llama area en formato float
    """
    area = lado*lado
    return area

def area_circulo(radio):
    """
    Calcula el area del circulo y retorna una variable
    que se llama area en formato float
    """
    area = math.pi*radio**2
    return area

def area_triangulo(base,altura):
    """
    Calcula el area del triangulo y retorna una variable
    que se llama area en formato float
    """
    area = (base*altura)/2
    return area