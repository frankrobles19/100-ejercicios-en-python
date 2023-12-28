#Hacer un algoritmo que muestre una gráfica de asteriscos [ * ] 
xn = 7
for f in range(7):
    serie = ""
    if (f >= 5):
        xn = xn + 2
    for c in range(xn - f):
        print(serie, end= "*")

    print()