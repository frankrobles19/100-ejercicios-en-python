#  Hacer un algoritmo que dibuje un triangulo con un carácter ingresado

def dibujar_triangulo(caracter, altura):
    for i in range(1, altura + 1):
        espacios = altura - i
        triangulo = ' ' * espacios + caracter * (2 * i - 1)
        print(triangulo)

# Solicitar al usuario el carácter y la altura del triángulo
caracter = input("Ingrese el carácter para el triángulo: ")
altura = int(input("Ingrese la altura del triángulo: "))

dibujar_triangulo(caracter, altura)
