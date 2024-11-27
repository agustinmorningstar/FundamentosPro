# Solicitar el resultado del dado al usuario
resultado = int(input("Introduce el resultado del dado (1 a 6): "))

# Diccionario para convertir el número a texto
numeros_a_letras = {
    1: "uno",
    2: "dos",
    3: "tres",
    4: "cuatro",
    5: "cinco",
    6: "seis"
}

# Diccionario para las caras opuestas
caras_opuestas = {
    1: 6,
    2: 5,
    3: 4,
    4: 3,
    5: 2,
    6: 1
}

# Validar el resultado y determinar la cara opuesta
if 1 <= resultado <= 6:
    cara_opuesta = caras_opuestas[resultado]
    cara_opuesta_letras = numeros_a_letras[cara_opuesta]
    print(f"La cara opuesta al {numeros_a_letras[resultado]} es {cara_opuesta_letras}.")
else:
    print("ERROR: número incorrecto.")
