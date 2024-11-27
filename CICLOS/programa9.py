'''
Escribir un programa que imprima todos los números pares entre dos números que 
se le pidan al usuario.
'''

N1 = int(input("Introduce el primer número: "))
N2 = int(input("Introduce el primer número: "))

if N1 > N2:
    N1, N2 = N2, N1

for numero in range(N1, N2+1):
    if numero % 2 == 0:
        print(numero)