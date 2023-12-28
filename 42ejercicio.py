#  Algoritmo que ingrese un total de segundos y muestre cuantas horas, minutos y segundos hay.

# Ingresar el total de segundos
total_segundos = int(input("Ingrese el total de segundos: "))

# Calcular horas, minutos y segundos
horas = total_segundos // 3600
minutos = (total_segundos % 3600) // 60
segundos = total_segundos % 60

# Mostrar el resultado
print(f"{total_segundos} segundos son equivalentes a:")
print(f"Horas: {horas}")
print(f"Minutos: {minutos}")
print(f"Segundos: {segundos}")
