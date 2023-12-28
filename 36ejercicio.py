# VALORES SUPERIORES : 4 – 9 – 15 – 23 – 34 – 49 ...
# x = 5
# v = 4 + 5 = 9
# v = 9 + 6 = 15
# v = 15 + 8 = 23
# v = 23 + 11 = 34
# v = 34 + 15 = 49

# Dónde x inicia en 5 : x = (x + 0), (x + 1), (x + 2), (x + 3), (x + 4) ...

# VALORES INFERIORES : 2 – 1 – 1 – 2 – 8 – 64 ...
# y = 0.5
# v = 2 * 0.5 = 1
# v = 1 * 1 = 1
# v = 1 * 2 = 2
# v = 2 * 4 = 8
# v = 8 * 8 = 64

# Dónde y inicia en 0.5 : y = (0.5 + 0.5), (1 + 1), (2 + 2), (4 + 4), (8 + 8) ... 
 


def generar_serie_superior(n):
    x = 5
    v = 4

    for i in range(n):
        if i != 0:
            print("-", end=" ")

        print(v, end=" ")
        v += x
        x += 1

def generar_serie_inferior(n):
    y = 0.5
    v = 2

    for i in range(n):
        if i != 0:
            print("-", end=" ")

        print(v, end=" ")
        v *= y
        y += 0.5

try:
    n = int(input("Ingrese el valor de n: "))

    print("VALORES SUPERIORES:", end=" ")
    generar_serie_superior(n)

    print("\nVALORES INFERIORES:", end=" ")
    generar_serie_inferior(n)

except ValueError:
    print("Ingrese un número válido.")
