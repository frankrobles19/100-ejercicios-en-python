#  Introduce 3 notas y calcula el promedio de un estudiante. Según el promedio obtenido, obtén el nivel académico del estudiante :
# * De 00 a 10 = Malo.
# * De 11 a 13 = Regular.
# * De 14 a 16 = Bueno.
# * De 17 a 20 = Muy bueno


nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

if 0 <= promedio <= 10:
    nivel_academico = "Malo"
elif 11 <= promedio <= 13:
    nivel_academico = "Regular"
elif 14 <= promedio <= 16:
    nivel_academico = "Bueno"
elif 17 <= promedio <= 20:
    nivel_academico = "Muy bueno"
else:
    nivel_academico = "Error: Promedio fuera de rango."

print(f"El promedio de las notas es: {promedio:.2f}")
print(f"Nivel académico: {nivel_academico}")
