# Ingresar una frase y mostrar la cantidad de vocales que contiene
frase = input("ingrese una frase")
Numvocal = 0
for vocal in frase:
    if vocal == "a":
       Numvocal += 1 
    if vocal == "e":
       Numvocal += 1
    if vocal == "i":
       Numvocal += 1
    if vocal == "o":
       Numvocal += 1
    if vocal == "u":
       Numvocal += 1

print(f"la canridad de vocales que hay son : {Numvocal}")