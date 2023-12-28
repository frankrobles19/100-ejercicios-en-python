
# (*) El programa:
# • Debe validar el ingreso del número de filas. Dato mayor o igual a 3.
# • El triángulo tiene tantas filas como indica el dato de entrada, y la cantidad de números que se imprime en cada fila aumenta de dos en dos,
#  en la primera fila hay un solo número, en la segunda fila hay 3 números, en la tercera fila hay 5 números y así sucesivamente.
# • Los números que se imprimen en cada fila empieza en 1 y van hasta el 9, luego se imprime del cero, uno, dos y hasta el número que corresponda.

# EJEMPLOS 1 :
# Filas : 1
# Filas : 0
# Filas : -2
# Filas : 7

#             1
#            123
#           12345
#          1234567
#         123456789
#        12345678901
#       1234567890123


def imprimir_triangulo(filas):
    # Validar que el número de filas sea mayor o igual a 3
    if filas < 3:
        print("El número de filas debe ser mayor o igual a 3.")
        return

    # Inicializar el número a imprimir en cada fila
    numero = 1

    for i in range(filas):
        # Imprimir espacios en blanco
        espacios = " " * (filas - i - 1)
        print(espacios, end="")

        # Imprimir números ascendentes
        for j in range(2 * i + 1):
            print(numero, end="")
            numero = (numero + 1) % 10

        print()  # Salto de línea al final de cada fila

# Solicitar al usuario el número de filas
try:
    filas = int(input("Ingrese el número de filas (mayor o igual a 3): "))
    imprimir_triangulo(filas)
except ValueError:
    print("Ingrese un número válido.")
