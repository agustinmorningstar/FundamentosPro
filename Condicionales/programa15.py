# Función para determinar el ganador
def determinar_ganador(j1, j2):
    if j1 == j2:
        return "Empate"
    elif (j1 == "piedra" and j2 == "tijera") or \
         (j1 == "papel" and j2 == "piedra") or \
         (j1 == "tijera" and j2 == "papel"):
        return "Gana el Jugador 1"
    else:
        return "Gana el Jugador 2"

# Leer las opciones de los jugadores
jugador1 = input("Jugador 1, elige piedra, papel o tijera: ").lower()
jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()

# Validar las opciones
opciones_validas = ["piedra", "papel", "tijera"]

if jugador1 not in opciones_validas or jugador2 not in opciones_validas:
    print("Opción incorrecta.")
else:
    # Determinar y mostrar el resultado
    resultado = determinar_ganador(jugador1, jugador2)
    print(f"Resultado: {resultado}")
