# Algoritmo que muestre el promedio de 3 notas y muestre si esta aprobado o desaprobado
def calcular_promedio(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def evaluar_aprobacion(promedio):
    if promedio >= 6:
        return "Aprobado"
    else:
        return "Desaprobado"

def main():
    try:
        # Solicitar al usuario ingresar las tres notas
        nota1 = float(input("Ingrese la primera nota: "))
        nota2 = float(input("Ingrese la segunda nota: "))
        nota3 = float(input("Ingrese la tercera nota: "))

        # Calcular el promedio
        promedio = calcular_promedio(nota1, nota2, nota3)

        # Mostrar el promedio
        print(f"El promedio de las notas es: {promedio:.2f}")

        # Evaluar y mostrar si está aprobado o desaprobado
        resultado = evaluar_aprobacion(promedio)
        print(f"Resultado: {resultado}")

    except ValueError:
        print("Por favor, ingrese notas válidas.")

if __name__ == "__main__":
    main()
