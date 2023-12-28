# algoritmo simple para calcular el descuento según el monto de compra 
monto_compra = float(input("Ingrese el monto de compra: "))

if monto_compra > 350:
    descuento = 0.35  
else:
    descuento = 0.10  
    
monto_descuento = monto_compra * descuento
monto_a_pagar = monto_compra - monto_descuento

# Mostrar resultados
print(f"Monto de compra: ${monto_compra:.2f}")
print(f"Descuento aplicado: ${monto_descuento:.2f}")
print(f"Monto a pagar: ${monto_a_pagar:.2f}")
