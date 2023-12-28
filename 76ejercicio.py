#  Elaborar un algoritmo que permita ingresar el nombre del trabajador, sueldo básicos y el número de hijos,
#  se debe mostrar su bonificación y el sueldo final. Tenga en cuenta que la empresa está dando una bonificación del 7% del sueldo básico,
#  sólo en el caso de que el trabajador tuviese hijos.

# Solicitar al usuario ingresar información del trabajador
nombre = input("Ingrese el nombre del trabajador: ")
sueldo_basico = float(input("Ingrese el sueldo básico: "))
num_hijos = int(input("Ingrese el número de hijos: "))

# Verificar si el trabajador tiene hijos para aplicar la bonificación
if num_hijos > 0:
    bonificacion = 0.07 * sueldo_basico
else:
    bonificacion = 0

# Calcular el sueldo final
sueldo_final = sueldo_basico + bonificacion

print(f"\nResumen para el trabajador {nombre}:")
print(f"Sueldo Básico: ${sueldo_basico:.2f}")
print(f"Bonificación (7% del sueldo básico): ${bonificacion:.2f}")
print(f"Sueldo Final: ${sueldo_final:.2f}")

