#  Hacer un algoritmo que muestre el nombre del mes, según el número ingresado del 1 al 12.

numero = int(input("Ingrese un número del 1 al 12: "))

if 1 <= numero <= 12:
    nombres_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Setiembre", "Octubre", "Noviembre", "Diciembre"]
    
    # Obtener el nombre del mes correspondiente al número ingresado
    nombre_mes = nombres_meses[numero - 1]

    print(f"\nEl número {numero} corresponde al mes: {nombre_mes}")
else:
    print("\nERROR: Ingrese un número válido del 1 al 12.")
