#  Una garita cobra por el paso de vehículos. El cobro se realiza de acuerdo al vehículo; hay tres tipos de vehículos
#  Ómnibus, Minivan y micro que su tarifa es de 13, 10, 8 soles respectivamente, 
# ingrese el tipo de vehículo y el turno (Mañana, Noche).

# Desarrollar un algoritmo que permita: Ingresar datos: La cantidad de vehículos,
#  de cada vehículo se debe ingresar el tipo y el turno (Mañana, Noche).

# A. Ingreso de datos.
# B. Calculo del importe total recaudado en cada turno.
# C. Calculo del importe total recaudado por cada tipo de vehículo.
import os 

dicMañana = {
    "omnibus" : 0,
    "minivan" : 0,
    "micro" : 0
}

dicNoche = {
    "omnibus" : 0,
    "minivan" : 0,
     "micro" :  0
}


omnibus = 13
minivan = 10
micro = 8



menu = "1. Registrar turno mañana\n2. Registrar turno noches\n3. ver recaudo mañana\n4. ver recaudo noche\n5. ver recaudo total por coche\n6. salir"
subMenu = "1.omnibus\n2.minivan\n3.micro"
hasError = True

while hasError == True :
    try:
        print(menu)
        opmenu = int(input("ingrese una opcion del menu: "))
        if opmenu == 1:
            print(subMenu)
            opmenu2 = int(input("ingrese una opcion del menu :"))
            if opmenu2 == 1:
                os.system("clear")
                bandera1 = True
                while bandera1 == True:
                    try:
                        cantMañanaOmnibus  = int(input("ingrese la cantidad de veiculos: "))
                        cantidadomnibus = cantMañanaOmnibus * omnibus 
                        print(cantidadomnibus)
                        dicMañana["omnibus"] += cantidadomnibus
                    except: 
                        print("error, solo se admiten numeros enteros, vuelva a intentarlo")
                    else:
                        bandera1 = bool(input("si desea seguir segistrando presione para si(s) o (enter) para no)"))
            elif opmenu2 == 2:
                os.system("clear")
                bandera1 = True
                while bandera1 == True:
                    try:
                        cantMañanaminivan = int(input("ingrese la cantidad de veiculos:  "))
                        cantidadminivan = cantMañanaminivan * minivan
                        dicMañana["minivan"] += cantidadminivan

                        print(cantidadminivan)
                    except: 
                        print("error, solo se admiten numeros enteros, vuelva a intentarlo")
                    else:
                        bandera1 = bool(input("si desea seguir segistrando presione para si(s) o enter para no)"))
            elif opmenu2 == 3:
                os.system("clear")
                bandera1 = True
                while bandera1 == True:
                    try:
                        cantMañanaMicro = int(input("ingrese la cantidad de veiculos: "))
                        cantidadMicro = cantMañanaMicro * micro
                        dicMañana["micro"] += cantidadMicro

                        print(cantidadMicro)
                    except: 
                        print("error, solo se admiten numeros enteros, vuelva a intentarlo")
                    else:
                        bandera1 = bool(input("si desea seguir segistrando presione para si(s) o (enter) para no)"))
        elif opmenu == 2:
                print(subMenu)
                opmenu2 = int(input("ingrese una opcion del menu: "))
                if opmenu2 == 1:
                    os.system("clear")
                    bandera2 = True
                    while bandera2 == True:
                        try:
                            cantnochesOmnibus = int(input("ingrese la cantidad de veiculos:  "))
                            cantidadomnibus = cantnochesOmnibus * omnibus
                            dicNoche["omnibus"] += cantidadomnibus
                            print(cantidadomnibus)
                        except: 
                            print("error, solo se admiten numeros enteros, vuelva a intentarlo")
                        else:
                            bandera2 = bool(input("si desea seguir segistrando presione para si(s) o (enter) para no)"))
                elif opmenu2 == 2:
                    os.system("clear")
                    bandera2 = True
                    while bandera2 == True:
                        try:
                            cantnochesminivan = int(input("ingrese la cantidad de veiculos:  "))
                            cantidadminivan = cantnochesminivan * minivan
                            dicNoche["minivan"] += cantidadminivan

                            print(cantidadminivan)
                        except: 
                            print("error, solo se admiten numeros enteros, vuelva a intentarlo")
                        else:
                            bandera2 = bool(input("si desea seguir segistrando presione para si(s) o (enter) para no)"))
                elif opmenu2 == 3:
                    os.system("clear")   
                    bandera2 = True
                    while bandera2 == True:
                        try:
                            cantnochesMicro = int(input("ingrese la cantidad de veiculos:  "))
                            cantidadMicro = cantnochesMicro * micro
                            dicNoche["micro"] += cantidadMicro

                            print(cantidadMicro)
                        except: 
                            print("error, solo se admiten numeros enteros, vuelva a intentarlo")
                        else:
                            bandera2 = bool(input("si desea seguir segistrando presione para si(s) o enter para no)"))
        elif opmenu == 3:
            os.system("clear")   
            print(dicMañana)
        elif opmenu == 4:
            os.system("clear")   
            print(dicNoche)   
        elif opmenu == 5:
            os.system("clear")   
            suma_dic_mañana = dicMañana.get("omnibus", 0)
            suma_dic_noche = dicNoche.get("omnibus", 0)
            sumdicOmnibus = int(suma_dic_mañana + suma_dic_noche)
            print(f"el total del coche omnibus fue : {sumdicOmnibus}")

            suma_dic_mañana = dicMañana.get("minivan", 0)
            suma_dic_noche = dicNoche.get("minivan", 0)
            sumdicMinivan = int(suma_dic_mañana + suma_dic_noche)
            print(f"el total del coche minivan fue : {sumdicMinivan}")

            suma_dic_mañana = dicMañana.get("micro", 0)
            suma_dic_noche = dicNoche.get("micro", 0)
            sumdicmicro = int(suma_dic_mañana + suma_dic_noche)
            print(f"el total del coche omnibus fue : {sumdicmicro}")
        elif opmenu == 6:
            os.system("clear")   
            print("gracias por usar el programa :D")
            hasError = False
    except:
        print("ha ocurrido un error, vuelva a intentar, solo numeros enteros")
    else:
        hasError == True