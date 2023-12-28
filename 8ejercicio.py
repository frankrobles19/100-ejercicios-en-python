# Hacer un algoritmo que muestre la serie gráfica de números 123456789 en forma decreciente
for i in range(8, 0, -1):
    for j in range(1, i+2):
        print(j, end="")
    print()
