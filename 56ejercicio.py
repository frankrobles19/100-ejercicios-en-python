# ALGORITMO QUE MUESTRA LA CANTIDAD DE AÑOS, MESES Y DÍAS QUE HAY EN UNA FECHA INGRESADA

fecha_ingresada = input("Ingrese la fecha en formato YYYY-MM-DD: ")

año, mes, dia = map(int, fecha_ingresada.split('-'))

import datetime
fecha_actual = datetime.datetime.now()

# Calcular la diferencia en años, meses y días
diferencia = fecha_actual - datetime.datetime(año, mes, dia)
dias_totales = diferencia.days

años = dias_totales // 365

dias_restantes = dias_totales % 365
meses = dias_restantes // 30

dias = dias_restantes % 30

print(f"Años: {años}, Meses: {meses}, Días: {dias}")
