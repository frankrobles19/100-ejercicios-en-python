# Hacer un programa que solicite el precio y la cantidad de compra;
# si el monto es mayor a S/.100 calcular el IGV. Mostrar el total a pagar y IGV si lo hubiera.
precio_unitario = float(input("Ingrese el precio unitario: "))
cantidad = int(input("Ingrese la cantidad de compra: "))

monto_total = precio_unitario * cantidad

# Verificar si el monto total es mayor a S/.100 para calcular el IGV
if monto_total > 100:
    igv = 0.18  # 18% de IGV
    monto_con_igv = monto_total * (1 + igv)
else:
    igv = 0
    monto_con_igv = monto_total

print(f"\nMonto total: S/.{monto_total:.2f}")
print(f"IGV aplicado ({igv * 100}%): S/.{monto_total * igv:.2f}")
print(f"Monto total con IGV: S/.{monto_con_igv:.2f}")
