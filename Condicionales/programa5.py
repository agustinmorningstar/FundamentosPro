# Programa que lee una cadena por teclado y comprueba si es una letra mayúscula del alfabeto.

# Solicitar al usuario que ingrese una cadena
cadena = input("Introduce una cadena: ")

# Definir el abecedario en mayúsculas
abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Comprobar si la cadena tiene solo una letra y está en el abecedario en mayúscula
if len(cadena) == 1 and cadena in abecedario:
    print("La cadena es una letra mayúscula del abecedario.")
else:
    print("La cadena no es una letra mayúscula del abecedario.")
    