# Hacer un algoritmo que muestre la serie : 1 + 2/3 + 3/5 + 4/7 usando PARA
def suma_series(n):
    suma = 0
    for i in range(1, n+1):
        suma += i / (2*i - 1)
    return suma

def main():
    n = int(input("Ingrese el valor de n: "))
    sums = suma_series(n)
    print("La suma de la serie es: ", sums)

if __name__ == "__main__":
    main()