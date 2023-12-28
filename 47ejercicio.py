# Hacer un algoritmo que muestre los días transcurridos desde el inicio del año hasta ahora

mes = int(input("ingrese numero de mes"))
dia = int(input("ingrese numero de dias"))

tiempo = (((mes -1)* 30) + dia)

print("los dias transcurridos son", tiempo)