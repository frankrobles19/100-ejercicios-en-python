
numero =  int(input("FACTORIAL A CALCULAR"))
factorial = 1
i = 1
while (i <= numero):
    factorial = factorial * i
    i = i + 1
print ("El factorial de " + str(numero) + " es " + str(factorial))
