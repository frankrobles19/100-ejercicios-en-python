# Genere un programa que permita calcular el sueldo final de un empleado, si se sabe que el sueldo aumenta en $100
# por cada hijo y en $25 por cada día no laborable que el trabajador asistió.
# Debe ingresar por teclado: el sueldo base, el número de hijos y el número de días no laborables que asistió el trabajador.
constante = 100
diaLaborable = 25
hijos = int(input("ingrese cuentos hijos tiene"))
DiasN = int(input("ingrese la cantidad de dias que no asistio"))
sBase = int(input("ingrese sueldo base"))
total1 = ((hijos*constante) + (diaLaborable*DiasN) + sBase)
print(f"el sueldo final es de {total1}")