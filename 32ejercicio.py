# Hacer un programa dónde se tienen 10 niños a quienes se les pide sus datos personales como DNI,
# Fecha de nacimiento (considerar día, mes y año) y género. 
# Si los niños tienen 8 años o más se les dará Tablet.
# Si los niños tienen 6 años se les dará carrito o muñeca dependiendo del género.
añoActual = 2023
bandera = True
while bandera == True:
    dni = input("Introduce el DNI: ")
    añoNacimiento = int(input("ingrese año de nacimiento"))
    mesNacimiento = int(input("Ingrese mes de nacimiento (1-12): "))
    díaNacimiento = int(input("Ingrese dia de nacimiento (1-31): "))
    género = str(input("Indica su género [M/F]: ")).upper()

    if (añoNacimiento - añoActual) >= 8:
        print("Tablet")
        bnadera = (bool(input("si desea seguir presion (s) si no entonces (enter)")))  
    elif (añoNacimiento - añoActual) <= 6:
        if género == 'M':
            print("Carro")
            bandera = (bool(input("si desea seguir presion (s) si no entonces (enter)")))  
        elif género == "F":
            print("Muñeca")
            bandera = (bool(input("si desea seguir presion (s) si no entonces (enter)")))  
