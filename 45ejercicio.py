#  Hacer un algoritmo que calcule las medidas de una pared según el alto y largo ingresado.

metroCuadrado = 0.25
largo = int(input("ingrese alto de la pared"))
alto =  int(input("largo de la pared"))

arena = (metroCuadrado*(largo*alto))
print("la arena necesaria es :", arena, "mt3")