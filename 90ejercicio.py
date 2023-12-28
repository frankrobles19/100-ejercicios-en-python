# Una compañía aseguradora ofrece a sus clientes tres opciones de seguro, [X – Y – Z]. Tipo de seguro – Costo mensual ($):
# X – $45
# Y – $30
# Z – $15

opciones_seguro = {
    'X': 45,
    'Y': 30,
    'Z': 15
}

opcion_seleccionada = input("Seleccione el tipo de seguro (X, Y, Z): ").upper()

if opcion_seleccionada in opciones_seguro:
    costo_mensual = opciones_seguro[opcion_seleccionada]
    print(f"\nEl costo mensual del seguro {opcion_seleccionada} es de ${costo_mensual}.")
else:
    print("\nERROR: Ingrese una opción de seguro válida (X, Y, Z).")
