#  Hacer un algoritmo que muestre todos los números que estén en el rango de A y B en pseint

numeroA = int(input("NUMERO A : "))
numeroB = int(input("NUMERO B : "))

if (numeroA < numeroB):
    for n in range(numeroA+1, numeroB-1):
        print(n)
else:
    for n in range(numeroB+1, numeroA-1):
        print(n)

