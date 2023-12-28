# Crea una variable para almacenar la primera letra de los siguientes lenguajes de programación:
# Visual Basic, Pascal, C#, Java, Fortran. Dependiendo de la letra ingresada,
# muestra el lenguaje de programación correspondiente en pantalla.
# Si la letra no pertenece a ningún lenguaje de programación, muestra un mensaje de error.

letra = input("Ingrese una letra: ")

lenguaje = ""

if letra.upper() == 'V':
    lenguaje = 'Visual Basic'
elif letra.upper() == 'P':
    lenguaje = 'Pascal'
elif letra.upper() == 'C':
    lenguaje = 'C#'
elif letra.upper() == 'J':
    lenguaje = 'Java'
elif letra.upper() == 'F':
    lenguaje = 'Fortran'
else:
    print("Error: La letra ingresada no corresponde a ningún lenguaje de programación.")

if lenguaje:
    print(f"El lenguaje de programación correspondiente a la letra {letra.upper()} es: {lenguaje}")
