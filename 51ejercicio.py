# Hacer un algoritmo que muestra el área y perímetro de un trapecio

print("AREA DEL TRAPESIO")
BaseMayor = int(input("ingrese base mayor:"))
BaseMenor = int(input("ingrese base menor:"))
altura = int(input("ingrese altura:"))

a = (((BaseMayor* BaseMenor) * altura) /2)

print("area: ", a, "cm2")

print("perimetro del trapesio")
lado1 = int(input("ingrese lado1:"))
lado2 = int(input("ingrese lado2:"))
lado3 = int(input("ingrese lado3:"))
lado4 = int(input("ingrese lado4:"))

p = lado1 + lado2 + lado3 + lado4
print("perimetro :", p , "cm")
