# Ingresa el salario de un empleado y su nivel jerárquico o categoría. Según su nivel jerárquico se le otorgará un bono adicional al salario neto a pagar.

# Categoría = Bonificación :
# A = 10%
# B = 20%
# C = 30%
# D = 50%

salario = float(input("Ingrese el salario del empleado: "))
categoria = input("Ingrese la categoría del empleado (A, B, C o D): ").upper()

if categoria == 'A':
    bonificacion = 0.10
elif categoria == 'B':
    bonificacion = 0.20
elif categoria == 'C':
    bonificacion = 0.30
elif categoria == 'D':
    bonificacion = 0.50
else:
    print("Error: Categoría no válida.")
    bonificacion = 0

salario_neto = salario * (1 + bonificacion)

if bonificacion > 0:
    print(f"El salario neto con bonificación para la categoría {categoria} es: ${salario_neto:.2f}")
