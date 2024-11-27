'''
Escribe un programa que dados dos números, uno real (base) y un entero positivo 
(exponente), saque por pantalla el resultado de la potencia. No se puede 
utilizar el operador de potencia.
'''

base = int(input("Introduce la base:"))
exponente = int(input("Introduce el exponente:"))

if exponente < 0:
    print("No hay potencias negativas lol")
else:
    resultado = 1

for _ in range(exponente):
    resultado *= base

print(f"El resultado es {resultado}")