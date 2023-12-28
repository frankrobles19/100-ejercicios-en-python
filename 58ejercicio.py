# HACER UN ALGORITMO QUE CALCULE EL ÁREA Y EL PERÍMETRO DE UN ROMBO
print("AREA DEL ROMBO")
diametroM = int(input("ingrese diametro mayor"))
diametroMenor = int(input("ingrese diametro menor"))

a = (diametroM * diametroMenor)/2
print("AREA :",a, "cm")
print("PERIMETRO DEL ROMBO")
lado = int(input("ingrese lado"))
p = 4 * lado

print("PERIMETRO:", p, "cm")
