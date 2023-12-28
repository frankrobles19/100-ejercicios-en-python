cantidadN = int(input("ingrese numero"))
par = 0 
impar = 0 
for i in range(cantidadN):

    if (i % 2) == 0:
        par = i + 1
        str1 = str(par)
        suma1 = sum(str1)
    else:
        impar =  i + 1
        str2 = str(impar)
        sum2 = sum(str2)
print(f"candidad pares es:  {suma1}")
print(f"cantiadad impares es : {sum2}")