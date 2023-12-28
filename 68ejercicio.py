# Algoritmo que muestra el porcentaje de alumnos aprobados y desaprobados.

aprobados = int(input("ingrese la cantidad de alumnos aprobados"))
desaprobados = int(input("ingrese la cantidad de alumnos desaprobados"))

sum = aprobados + desaprobados
porcentaje_aprobado = (aprobados / sum) * 100
porcentaje_desaprobado = (desaprobados / sum) * 100
print ("El porcentaje de alumnos aprobados es: ", porcentaje_aprobado, "%")
print ("El porcentaje de alumnos desaprobados es: ", porcentaje_desaprobado, "%")