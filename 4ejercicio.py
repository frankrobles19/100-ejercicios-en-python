#algoritmo que muestre el nombre y el promedio del alumno con la mejor nota
xhrgo = 0
for cont in range(1, 6):
    nom = input("NOMBRE: ")
    pro = float(input("PROMEDIO: "))
    if pro > xhrgo:
        xhrgo = pro
        xnom = nom
print("ALUMNO CON MAYOR NOTA:", xnom)
print("PROMEDIO:", xhrgo)

#         



