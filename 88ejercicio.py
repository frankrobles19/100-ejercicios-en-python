# Introducir dos números enteros y un operador (+, -, *, /); según el operador seleccionado, realizar y mostrar la operación matemática correspondiente

numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

operador = input("Ingrese un operador (+, -, *, /): ")

if operador == "+":
    resultado = numero1 + numero2
elif operador == "-":
    resultado = numero1 - numero2
elif operador == "*":
    resultado = numero1 * numero2
elif operador == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        print("ERROR: No se puede dividir entre cero.")
        resultado = None
else:
    print("ERROR: Ingrese un operador válido.")

if resultado is not None:
    print(f"\nResultado de la operación {numero1} {operador} {numero2}: {resultado}")
