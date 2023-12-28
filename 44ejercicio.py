#  Hacer un algoritmo que muestra el total a pagar por un préstamo del banco 

monto = float(input("ingrese el monto"))

meses = int(input("ingrese los meses que se va a demorar pagando joven"))
 
intereses = (1000*(meses*0.02))
total_a_pagar= monto + intereses
print ("El monto de intereses es : ", intereses)
print ("El monto total a pagar es : ", total_a_pagar)