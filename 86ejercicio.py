# Hacer un programa que ingrese un número del 1 al 4 y muestre a que estación del año pertenece en Perú.

# 1 = VERANO
# 2 = OTOÑO
# 3 = INVIERNO
# 4 = PRIMAVERA

numero = int(input("Ingrese un número del 1 al 4: "))

# Verificar si el número está en el rango permitido
if 1 <= numero <= 4:
    # Asignar la estación del año correspondiente al número ingresado
    estaciones = ["VERANO", "OTOÑO", "INVIERNO", "PRIMAVERA"]
    estacion_actual = estaciones[numero - 1]

    print(f"\nEl número {numero} corresponde a la estación del año: {estacion_actual}")
else:
    print("\nERROR: Ingrese un número válido del 1 al 4.")

