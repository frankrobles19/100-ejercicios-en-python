# Algoritmo que ingrese un refrán y muestre el número de letras C, S, D, L, R y M que hay
refran = input("ingrese un refran").lower()
c = 0
s = 0
d = 0
l = 0
r = 0
m = 0
vocales = 0
for i in refran:
    if i == "c":
        c += 1
        continue
    elif i == "s":
        s += 1
        continue
    elif i == "d":
        d += 1
        continue
    elif i == "l":
        l += 1
        continue
    elif i == "r":
        r += 1
        continue
    elif i == "m":
        m += 1
        continue
    elif i == "a":
        vocales = vocales + 1
    elif i == "e":
        vocales = vocales + 1
    elif i == "i":
        vocales = vocales + 1
    elif i == "o":
        vocales = vocales + 1
    elif i == "u":
        vocales = vocales + 1

       
print(f"el refrán contiene {c} c, {s} s, {d} d, {l} l, {r} r, {m} m")
print(f"numero DE VOCALES  son : {vocales}" )
    