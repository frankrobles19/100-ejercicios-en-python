# Hacer un algoritmo que calcule el IGV 18% del monto a pagar, si el monto es mayor a $500.

monto_a_pagar = float(input("Ingrese el monto a pagar: "))

if monto_a_pagar > 500:
    igv = 0.18  # 18% de IGV
    monto_con_igv = monto_a_pagar * (1 + igv)
else:
    igv = 0
    monto_con_igv = monto_a_pagar

# Mostrar resultados
print(f"\nMonto a pagar: ${monto_a_pagar:.2f}")
print(f"IGV aplicado ({igv * 100}%): ${monto_a_pagar * igv:.2f}")
print(f"Monto total con IGV: ${monto_con_igv:.2f}")
