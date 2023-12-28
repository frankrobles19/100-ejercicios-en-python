#  Hacer un programa que al ingresar un número entero permita mostrar el triángulo de pascal.

# Ingrese Número : 5

#         1
#        1 1
#       1 2 1
#      1 3 3 1
#     1 4 6 4 1

def calcular_coeficientes(n):
    coeficientes = []

    for i in range(n):
        fila = [1] * (i + 1)

        if i > 1:
            for j in range(1, i):
                fila[j] = coeficientes[i - 1][j - 1] + coeficientes[i - 1][j]

        coeficientes.append(fila)

    return coeficientes

def imprimir_triangulo_pascal(coeficientes):
    max_digitos = len(str(max(map(max, coeficientes))))  # Determina el número máximo de dígitos para alinear la salida

    for fila in coeficientes:
        espacios = " " * max_digitos  # Inicializa espacios en blanco para alineación
        print(espacios * (len(coeficientes) - len(fila)), end="")  # Ajusta espacios para alineación

        for coeficiente in fila:
            print(f"{espacios}{coeficiente}", end=" ")
            espacios = " " * (max_digitos - len(str(coeficiente)))  # Ajusta espacios para alineación

        print()  # Salto de línea al final de cada fila

try:
    n = int(input("Ingrese un número entero para generar el Triángulo de Pascal: "))
    coeficientes = calcular_coeficientes(n)
    imprimir_triangulo_pascal(coeficientes)
except ValueError:
    print("Por favor, ingrese un número entero válido.")
