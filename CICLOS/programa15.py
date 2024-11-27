'''
Realizar un programa que pida al usuario un número entero y muestre el mismo número en binario
'''
numero = int(input("Introduce un número entero: "))

if numero == 0:
    print("El número en binario es: 0")
else:
    binario = ""
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2

    print("El número en binario es:", binario)