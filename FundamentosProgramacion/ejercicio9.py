# 9. Cálculo de pago final con descuento
total_compra = float(input("Ingrese el total de la compra: "))
descuento = total_compra * 0.15
total_final = total_compra - descuento
print("Total a pagar:", total_final)