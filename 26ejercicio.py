# Algoritmo que muestra todos los números que son capicúa de tres cifras
tresDigitos = [i for i in range(100, 1000)]
string_Numeros = [str(i) for i in tresDigitos]
palindromes = [i for i in string_Numeros if i == i[::-1]]
print(palindromes)

