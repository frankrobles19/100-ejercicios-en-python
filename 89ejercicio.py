# Calcular el costo de una llamada telefónica en función de la zona de destino y la duración de la llamada, y mostrar el total a pagar por los minutos consumidos según la zona a llamar :

# ZONA – COSTO:
# -----------------------------------------------
# [1] Estados Unidos – $. 0.13
# [2] Canadá – $. 0.11
# [5] América del Sur – $. 0.52
# [6] América Central – $. 0.99
# [8] México – $. 0.17
# [9] Europa – $. 0.17
# [10] Asia – $. 0.20
# [15] África – $. 0.59
# [20] Oceanía – $. 0.28

zonas = {
    1: ("Estados Unidos", 0.13),
    2: ("Canadá", 0.11),
    5: ("América del Sur", 0.52),
    6: ("América Central", 0.99),
    8: ("México", 0.17),
    9: ("Europa", 0.17),
    10: ("Asia", 0.20),
    15: ("África", 0.59),
    20: ("Oceanía", 0.28)
}

zona_destino = int(input("Ingrese la zona de destino (número): "))
duracion_llamada = float(input("Ingrese la duración de la llamada en minutos: "))

if zona_destino in zonas:
    nombre_zona, costo_por_minuto = zonas[zona_destino]

    costo_total = costo_por_minuto * duracion_llamada

    print(f"\nCosto total de la llamada a la zona {zona_destino} ({nombre_zona}): ${costo_total:.2f}")
else:
    print("\nERROR: Ingrese una zona de destino válida.")
