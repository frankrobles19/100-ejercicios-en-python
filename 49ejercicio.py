# Hacer un algoritmo que muestre el área y perímetro de un hexágono

perimetro = int(input("ingrese perimetro"))
apotema = int(input("ingrese apotema"))

a = (perimetro * apotema)/2

print("area", a,  "cm2")
print("perimetro del hexagono")
lado = int(input("lado"))

p = 6 * lado

print("perimetro :", p, "cm")