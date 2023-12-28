#  Hacer un algoritmo que muestre la cantidad de número pares e impares ingresados 

par = 0
impar = 0

for contador in range(1,11):
    numeros = int(input("ingrese un numero"))
    if numeros % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"cantidad de pares es: {par}")
print(f"cantidad de impares es: {impar}")
    

