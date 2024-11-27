'''
Crea un programa que permita adivinar un número. La aplicación genera un 
número aleatorio del 1 al 100. A continuación va pidiendo números y va 
respondiendo si el número a adivinar es mayor o menor que el introducido,
a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). 
El programa termina cuando se acierta el número (además te dice en cuantos 
intentos lo has acertado), si se llega al limite de intentos te muestra el 
número que había generado.
Para genear un número entero aleatorio se utiliza la función randint
del paquete random

import random
aleatorio = random.randint(limite_inf, limite_sup)
'''
import random

nAdivinar = random.randint(1, 100)

intentos = 10

print("Tienes 10 intentos para adivinar el número entre 1 y 100.")

while intentos > 0:
    intento = int(input(f"\nTe quedan {intentos} intentos. Ingresa tu número: "))

    if intento == nAdivinar:
        print(f"¡Felicidades! Adivinaste el número {nAdivinar} en {11 - intentos} intentos.")
        break
    elif intento < nAdivinar:
        print("El número a adivinar es mayor.")
    else:
        print("El número a adivinar es menor.")

    intentos -= 1
if intentos == 0:
    print(f"\n¡Lo siento! Te has quedado sin intentos. El número era {nAdivinar}.")
