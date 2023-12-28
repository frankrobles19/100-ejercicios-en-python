# Hacer un programa que ingrese un número del 1 al 10 y muestre el mismo número pero en Romanos.

# EJEMPLO :
# -----------------
# 1 = 1
# 2 = II
# 3 = III
# 4 = IV
# 5 = V
# 6 = VI
# 7 = VII
# 8 = VIII
# 9 = IX
# 10 = X

numero = int(input("Ingrese un número del 1 al 10: "))

# Verificar si el número está en el rango permitido
if 1 <= numero <= 10:
    simbolos_romanos = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
    
    # Obtener el símbolo romano correspondiente al número ingresado
    numero_romano = simbolos_romanos[numero - 1]

    print(f"\n{numero} = {numero_romano}")
else:
    print("\nERROR: Ingrese un número válido del 1 al 10.")
