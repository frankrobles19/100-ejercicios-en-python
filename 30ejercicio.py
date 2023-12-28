empleados = int(input("ingrese numero de empleados"))
ventasH = 0
ventasM = 0
mujeres = 0 

for i in range(empleados):
    print(f"EMPLEADO {i} / {empleados}")
    nombre = input("ingrese nombre")
    genero = input("ingrese su genero hombre (H) o mujer (M)").lower()
    ventas = int(input("ingrese ventas"))
    if genero == "h":
        ventasH = ventasH + ventas
    elif genero == "m":
        ventasM = ventasM + ventas 
        mujeres = mujeres + 1   
print(f"TOTAL VENTAS HOMBRES ES: {ventasH}")
print(f"TOTAL VENTAS MUJERES ES: {ventasM}")
print(f"PORCENTAJE DE MUJERES VENDEDORAS ES : {(mujeres*100)/empleados}")

