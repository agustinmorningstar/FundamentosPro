# Diccionario para mapear números a días de la semana
dias_semana = {
    1: "lunes",
    2: "martes",
    3: "miércoles",
    4: "jueves",
    5: "viernes",
    6: "sábado",
    7: "domingo"
}

# Solicitar al usuario un número del 1 al 7
dia_numero = int(input("Introduce un número del 1 al 7 para indicar el día de la semana: "))

# Verificar si el número está en el rango válido
if 1 <= dia_numero <= 7:
    print(f"El día correspondiente es {dias_semana[dia_numero]}.")
else:
    print("ERROR: número incorrecto.")
