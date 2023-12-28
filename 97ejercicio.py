# Hacer un programa dónde en una tienda que se venden teclados, si se compran más de 8 el costo por cada una es de 10 soles; entre 4 y 8 es de 11 soles cada una, si la compra es menor de 4 el costo es de 15 soles cada una.

cantidad_teclados = int(input("Ingrese la cantidad de teclados comprados: "))

if cantidad_teclados > 8:
    costo_por_teclado = 10
elif 4 <= cantidad_teclados <= 8:
    costo_por_teclado = 11
else:
    costo_por_teclado = 15

costo_total = cantidad_teclados * costo_por_teclado

print(f"Número de teclados: {cantidad_teclados}")
print(f"Costo por teclado: {costo_por_teclado} soles")
print(f"Costo total a pagar: {costo_total} soles")
