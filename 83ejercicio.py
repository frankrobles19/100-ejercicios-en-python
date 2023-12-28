# Hacer un algoritmo que muestre si un número es positivo o negativo

numero = float(input("Ingrese un número: "))

if numero > 0:
    print(f"El número {numero} es positivo.")
elif numero < 0:
    print(f"El número {numero} es negativo.")
else:
    print("El número ingresado es cero.")
