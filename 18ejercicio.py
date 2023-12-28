# Algoritmo que muestra si un número es o no capicúa
def es_palindromo(numero):
    # Convertir el número a una cadena
    num_str = str(numero)
    # Invertir la cadena
    cadena_invertida = num_str[::-1]
    # Comparar la cadena original con la cadena invertida
    if num_str == cadena_invertida:
        return True
    else:
        return False

# Obtener el número de entrada del usuario
numero = int(input("Ingrese un número: "))

# Verificar si el número es un palíndromo
if es_palindromo(numero):
    print(f"{numero} es un palíndromo.")
else:
    print(f"{numero} no es un palíndromo.")
