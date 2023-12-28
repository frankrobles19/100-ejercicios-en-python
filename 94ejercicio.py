#  Crea una aplicación donde una tienda vende teclados. Si se compran más de 8 teclados, el costo por unidad es de 10 soles, si se compran entre 4 y 8 el costo por unidad es de 11 soles, y si se compran menos de 4 el costo es de 15 soles por unidad. Diseña un algoritmo para calcular el costo total a pagar según la cantidad de teclados comprados. Muestra el número de teclados y el costo total en pantalla.

cantidad_teclados = int(input("Ingrese la cantidad de teclados comprados: "))

if cantidad_teclados > 8:
    costo_por_unidad = 10
elif 4 <= cantidad_teclados <= 8:
    costo_por_unidad = 11
else:
    costo_por_unidad = 15

costo_total = cantidad_teclados * costo_por_unidad

print(f"Número de teclados: {cantidad_teclados}")
print(f"Costo total a pagar: {costo_total} soles")
