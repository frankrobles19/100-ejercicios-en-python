# Hacer un algoritmo que muestre el número intermedio de tres números ingresados
# Solicitar al usuario ingresar tres números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

if numero1 <= numero2 <= numero3 or numero3 <= numero2 <= numero1:
    numero_intermedio = numero2
elif numero2 <= numero1 <= numero3 or numero3 <= numero1 <= numero2:
    numero_intermedio = numero1
else:
    numero_intermedio = numero3

print(f"El número intermedio es: {numero_intermedio}")
