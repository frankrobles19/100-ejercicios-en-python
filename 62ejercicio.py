costo = int(input("costo de la casa: "))
valorIva = int(input("valoe del iva"))

total = costo + (costo*(valorIva/100))
print("IVA DE", valorIva, "% :", (costo*(valorIva/100)))
print("TOTAL A PAGAR :", total)