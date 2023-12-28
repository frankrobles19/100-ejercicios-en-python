# Algoritmo que genere 10 números aleatorios que estén en el rango de 10 a 99
import random

N = int(input("Ingrese un número entero: "))
for i in range(N):
    print(random.randint(10, 90))


