# Hacer un programa que asigna una determinada bonificación a sus empleados según el monto total de sus venta, si el monto total de las ventas es mayor a $2000 asignar una bonificación del 10%, caso contrario dar una bonificación del 5%.

monto_ventas = float(input("Ingrese el monto total de ventas: "))

if monto_ventas > 2000:
    bonificacion = 0.10  # 10% de bonificación si el monto es mayor a $2000
else:
    bonificacion = 0.05  # 5% de bonificación en otros casos


monto_bonificacion = monto_ventas * bonificacion

print(f"\nMonto total de ventas: ${monto_ventas:.2f}")
print(f"Bonificación aplicada ({bonificacion * 100}%): ${monto_bonificacion:.2f}")
