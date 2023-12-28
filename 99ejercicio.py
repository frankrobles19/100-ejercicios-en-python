# Ejercicio 7: Contar la cantidad de vocales en una palabra
palabra = input("Ingrese una palabra: ")
vocales = 0

for letra in palabra:
    if letra.lower() in 'aeiou':
        vocales += 1