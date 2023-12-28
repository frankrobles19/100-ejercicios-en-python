# Hacer un programa dónde el presupuesto anual de un hospital se distribuya en las siguientes áreas : Ginecología 40%, Traumatología 30% y Pediatría 30%, de un monto total de dinero asignado.
presupuesto = int(input("ingrese presupuesto : "))
gine = presupuesto * 0.40
trau = presupuesto * 0.30
pedi = presupuesto * 0.30

print("GINECOLOGIA    :$", gine)
print("TRAUMATOLOGIA  :$", trau)
print("PEDIATRIA      :$", pedi)
