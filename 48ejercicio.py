# Hacer un algoritmo que muestre la unidad, la decena y la centena

num = int(input("ingrese un numero de 3 cifras"))

cen = (num - (num % 100))/100
res = num % 100
dec = (res - (res % 10))/10
uni = res % 10

print("centena", cen)
print("decena", dec)
print("unidad", uni)