numero = input("Ingrese un número: ")

# Verificar si el número es capicúa
if numero == numero[::-1]:
    print(f"El número {numero} es capicúa.")
else:
    print(f"El número {numero} no es capicúa.")
