#  Se cuenta con N personas para hacer una prueba, la cantidad de N personas es ingresa por el usuario.
# A cada persona se le pide que diga cuál de estos tres colores (Rojo, Verde o Azul) es su preferido y no puede responder ninguno.
# Se necesita calcular e informar la cantidad de personas que eligió cada color y cuál de los colores es el más elegido.

# Resuelve usando PARA. 
colores = {
    "rojo" : 0,
    "verde": 0,
    "azul": 0,
}


bandera = True
menu = ("1. ROJO \n2. VERDE\n3. AZUL ") 
Npersonas = int(input("ingrese un numero de personas que van a participar"))
for i in range (Npersonas):
    print(f"PERSONA {i +1} / {Npersonas }")
    print(menu)
    while bandera == True:
        try:
            opmenu = int(input("ingrese una opcion de color : "))
            if opmenu == 1:
                colores["rojo"] += 1
            elif opmenu == 2:
                colores["verde"] += 1
            elif opmenu == 3:
                colores["azul"] += 1        
        except:
            print("error!!, solo puede ingresar un numero entero")
        else:
            if 0 < opmenu <= 3 :
                break
            elif 0 > opmenu >=3:
                continue


logitudRojo = colores.get("rojo", 0)
logitudverde = colores.get("verde", 0)
logitudAzul = colores.get("azul", 0) 
if logitudRojo > max(logitudAzul,logitudverde):
    colorMax = "rojo"
elif logitudverde > max(logitudAzul, logitudRojo):
    colorMax = "verde"
else:
    colorMax = "azul"

print(" el color mas votado fue :", colorMax)
print(f"la cantidad de personas que escojio el rojo fue {colores['rojo']}")
print(f"la cantidad de personas que escojio el verde fue {colores['verde']}")
print(f"la cantidad de personas que escojio el azul fue {colores['azul']}")
