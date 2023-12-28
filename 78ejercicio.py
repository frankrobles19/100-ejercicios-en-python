# Hacer un programa que permita ingresar dos números y los muestre de forma ordenada de mayor a menor

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

if numero1 < numero2:
    mayor = numero2
    menor = numero1
else:
    mayor = numero1
    menor = numero2


print(f"\nNúmeros ordenados de mayor a menor: {mayor}, {menor}")
