precio = 500
"""
#O comparación
print(precio > 500) #F
print(precio >= 500) #V
print(precio < 500) #F
print(precio <= 500) #V
print(precio == 500) #V
print(precio != 500) #F
"""
#Compuertas logicas
#AND
print("---------AND-----------")
print(False and False) #0
print(False and True) #0
print(True and False) #0
print(True and True) #1
print("---------NAND-----------")
#NAND
print(not(False and False)) #1
print(not(False and True)) #1
print(not(True and False)) #1
print(not(True and True)) #0
print("----------OR-----------")
#OR
print(False or False) #0
print(False or True) #1
print(True or False) #1
print(True or True) #1
print("-----------NOR----------")
#NOR
print(not(False or False)) #1
print(not(False or True)) #0
print(not(True or False)) #0
print(not(True or True)) #0
print("-----------NOT----------")
print(not(False)) #1
print(not(True)) #0