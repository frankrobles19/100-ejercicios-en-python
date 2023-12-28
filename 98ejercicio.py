# Ingresar un número entero de dos cifras y mostrar su valor en letras
numero = int(input("Ingrese un número entero de dos cifras: "))

if 10 <= numero <= 99:
    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]

    unidad = numero % 10
    decena = numero // 10

    if decena == 1 and unidad > 0:
        numero_en_letras = f"{decenas[decena]} y {unidades[unidad]}"
    else:
        numero_en_letras = f"{decenas[decena]} {unidades[unidad]}"

    print(f"El número {numero} en letras es: {numero_en_letras}")
else:
    print("Error: Ingrese un número entero de dos cifras.")
