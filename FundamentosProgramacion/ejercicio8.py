# 8. Cálculo de comisiones y sueldo total
sueldo_base = float(input("Ingrese el sueldo base: "))
venta1 = float(input("Ingrese el monto de la primera venta: "))
venta2 = float(input("Ingrese el monto de la segunda venta: "))
venta3 = float(input("Ingrese el monto de la tercera venta: "))
comision = (venta1 + venta2 + venta3) * 0.10
total = sueldo_base + comision
print("Comisiones:", comision)
print("Total a recibir:", total)