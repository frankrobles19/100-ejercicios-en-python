#algoritmo que calcule el monto a pagar por 10 compras 
total = 0 
desc = 0 

for cont in range(1,11):
    consumo = int(input("CONSUMO : "))
    total = total + consumo 

if (total > 50):
    desc = total * 0.07
print("total a pagar sin descuento es :", total )
print ("descuento :", desc)
print (" total a pagar con descuento es :", total - desc)