# Hacer un algoritmo que muestre si un número es paro impar  
def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

def main():
    try:
        # Solicitar al usuario ingresar un número
        numero = int(input("Ingrese un número: "))

        # Determinar si es par o impar
        resultado = es_par_o_impar(numero)
        print(f"El número {numero} es {resultado}.")

    except ValueError:
        print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
