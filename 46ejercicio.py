# Hacer un algoritmo que al ingresar las horas, minutos y segundos, calcule el costo total.
horas = int(input("ingrese horas"))
minutos = int(input("ingrese minutos"))
segundos = int(input("ingrese segundos"))

costo = ((horas * 3600) + (minutos * 60) + segundos)* 0.25
print("total a pagar es", costo)

