# Hacer un algoritmo que muestre el área y volumen de un cilindro
radio = int(input("ingrese radio: "))
altura = int(input("ingrese altura: "))
a = 2* 3,14* radio*(altura + radio)
v = 3,14 * (radio * radio) * altura
print("AREA TOTAL DEL CILINDRO ES :", a, "cm2")
print("VOLUMEN TOTAL DEL CILINDRO ES :", v, "cm3")
