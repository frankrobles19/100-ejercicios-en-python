# Ejercicio 8: Sumar los primeros N números naturales
n = int(input("Ingrese un número entero positivo (N): "))
suma = sum(range(1, n + 1))
print(f"La suma de los primeros {n} números naturales es: {suma}")