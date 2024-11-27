# Solicitar duración de la llamada y día/turno
duracion = int(input("Introduce la duración de la llamada en minutos: "))
dia = input("¿Qué día se realizó la llamada? (domingo/otro): ").lower()
turno = "n/a"  # Inicialización

# Si el día no es domingo, se pide el turno
if dia != "domingo":
    turno = input("¿En qué turno se realizó la llamada? (mañana/tarde): ").lower()

# Calcular el costo base de la llamada según la duración
costo_base = 0

if duracion <= 5:
    costo_base = duracion * 1
elif duracion <= 8:
    costo_base = 5 * 1 + (duracion - 5) * 0.80
elif duracion <= 10:
    costo_base = 5 * 1 + 3 * 0.80 + (duracion - 8) * 0.70
else:
    costo_base = 5 * 1 + 3 * 0.80 + 2 * 0.70 + (duracion - 10) * 0.50

# Calcular el impuesto según el día y turno
impuesto = 0
if dia == "domingo":
    impuesto = costo_base * 0.03
else:
    if turno == "mañana":
        impuesto = costo_base * 0.15
    elif turno == "tarde":
        impuesto = costo_base * 0.10

# Calcular el costo total
costo_total = costo_base + impuesto

# Mostrar los resultados
print("\nDetalles del costo de la llamada:")
print(f"Costo base: {costo_base:.2f} euros")
print(f"Impuesto aplicado: {impuesto:.2f} euros")
print(f"Costo total de la llamada: {costo_total:.2f} euros")
