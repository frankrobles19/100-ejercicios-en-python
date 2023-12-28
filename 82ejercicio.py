# Hacer un algoritmo que muestre si un número ingresado es par o impar 

numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:
    print(f"\nEl número {numero} es par.")
else:
    print(f"\nEl número {numero} es impar.")
