# Diccionario para mapear números de meses a días
dias_mes = {
    1: 31,  # Enero
    2: 28,  # Febrero (no se considera año bisiesto)
    3: 31,  # Marzo
    4: 30,  # Abril
    5: 31,  # Mayo
    6: 30,  # Junio
    7: 31,  # Julio
    8: 31,  # Agosto
    9: 30,  # Septiembre
    10: 31, # Octubre
    11: 30, # Noviembre
    12: 31  # Diciembre
}

# Solicitar al usuario un número del 1 al 12
mes_numero = int(input("Introduce un número del 1 al 12 para indicar el mes: "))

# Verificar si el número está en el rango válido
if 1 <= mes_numero <= 12:
    print(f"El mes {mes_numero} tiene {dias_mes[mes_numero]} días.")
else:
    print("ERROR: número incorrecto.")
