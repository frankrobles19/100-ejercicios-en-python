# En la tienda de comestibles, los clientes deben pulsar un botón al realizar sus compras. Dependiendo del color de la luz que se encienda, recibirán un porcentaje de descuento en función del valor total de su compra, según lo indicado en la tabla de precios.

# Color = Descuento (%)
# ————————
# Blanco = 100%
# Verde = 50%
# Negro = 40%
# Celeste = 5%
# Rojo = 0%

color_luz = input("Ingrese el color de la luz (Blanco, Verde, Negro, Celeste o Rojo): ").capitalize()
valor_compra = float(input("Ingrese el valor total de su compra: "))

if color_luz == 'Blanco':
    descuento_porcentaje = 100
elif color_luz == 'Verde':
    descuento_porcentaje = 50
elif color_luz == 'Negro':
    descuento_porcentaje = 40
elif color_luz == 'Celeste':
    descuento_porcentaje = 5
elif color_luz == 'Rojo':
    descuento_porcentaje = 0
else:
    print("Error: Color de luz no válido. No se aplicará descuento.")
    descuento_porcentaje = 0

descuento = valor_compra * (descuento_porcentaje / 100)
total_pagar = valor_compra - descuento

print(f"Descuento aplicado ({color_luz}): {descuento:.2f} soles ({descuento_porcentaje}%)")
print(f"Total a pagar: {total_pagar:.2f} soles")
