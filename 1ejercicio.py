#Hacer un algoritmo que muestre la tabla de multiplicar de cualquier número ingresado.

Numero = int(input("Ingrese un número: "))
if Numero > 0:
    if isinstance(Numero, int):
        for i in range(1, 11):
            rta = Numero * i
            print(f"{Numero} * {i} = {rta}")
else:
    print("Ingrese un número mayor a 0")

