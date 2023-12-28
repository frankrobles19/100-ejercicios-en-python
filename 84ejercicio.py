# Realizar un algoritmo que al ingresar un número del 1 al 7, 
# muestre el día de la semana correspondiente siendo el 1 para el Lunes,
# de lo contrario mostrar un mensaje de ERROR.

numero_dia = int(input("Ingrese un número del 1 al 7: "))

# Verificar el día de la semana correspondiente
if 1 <= numero_dia <= 7:
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    dia_semana = dias_semana[numero_dia - 1]
    print(f"\nEl número {numero_dia} corresponde al día de la semana: {dia_semana}.")
else:
    print("\nERROR: Ingrese un número válido del 1 al 7.")
