'''
Escribe un programa que diga si un número introducido por teclado es o no primo. 
Un número primo es aquel que sólo es divisible entre él mismo y la unidad. 
Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es 
divisible por algún otro número.
'''
import math

num = int(input("Introduce un número: "))

if num < 2:
    print(f"{num} no es un número primo.")
else:
    es_primo = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"{num} es un número primo.")
    else:
        print(f"{num} no es un número primo.")