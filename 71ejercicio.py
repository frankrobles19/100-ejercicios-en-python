# Hacer un programa que simule un login o clave de acceso

def acceso(nombre, clave):
    if nombre == "admin" and clave == 1234567:
        return "ACCESO PERMITIDO"
    else:
        return "ERROR DE ACCESO. INTENTE NUEVAMENTE."

def main():
    bandera1 = True
    while bandera1 == True:
        try:
            nombre = input("Ingrese su nombre de usuario: ")
            clave = int(input("Ingrese su contraseña: "))
            resultado = acceso(nombre, clave)
            print(resultado)
        except ValueError:
            print("Error en la entrada de datos, intente de nuevo")
        else:
                continuar = input("Desea intentarlo nuevamente? s/n: ").lower()
                if continuar == "s":
                    bandera1 = False
                    break
                elif continuar == "n":
                    bandera1 = True

if __name__ == "__main__":
    main()



