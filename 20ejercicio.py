# Hacer un algoritmo que busque un número que se ha generado de forma aleatoria 
import random

numaleatorio = random.randint(1, 21)
for i in range(-5,0):
    print(f"encuentre el numero de 1 a 20, tiene {i} oportunidades")
    numero = int(input("ingrese el numero"))
    if (numaleatorio == numero):
        print("felicidades numero encontrado")
else:
 print(f"el numero era {numaleatorio}")   