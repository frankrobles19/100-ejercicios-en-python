# Dado la duración (en minutos) de una llamada telefónica, calcular su costo, de la siguiente manera: 
# Hasta 5 min el costo es 0.90. Por encima de 5 min el, costo es 0.90+0.20 por cada minuto adicional a los 5 primeros min.
# Escribir un programa que lea la duración de la llamada y calcule el costo de la misma

cantidadM = int(input("ingrese cantidad de minutos"))

if (cantidadM <= 5):
    costo = cantidadM*0.9
else: 
    costo = (5*0.9)+((cantidadM -5)*1.1)
    print ("el costo es", costo)