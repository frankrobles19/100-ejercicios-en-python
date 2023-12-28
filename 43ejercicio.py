# Algoritmo que muestre cuantas entradas al cine se pueden comprar con un monto ingresado.


monto_disponible = float(input("Ingrese el monto disponible: "))
precio_entrada = float(input("Ingrese el precio de la entrada al cine: "))
# Calcular la cantidad de entradas que se pueden comprar
entradas_comprables = int(monto_disponible // precio_entrada)
print(f"Con ${monto_disponible} puedes comprar {entradas_comprables} entradas al cine.")
