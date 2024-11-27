'''
Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' 
en caso contrario, el programa termina cuando se introduce un espacio.
'''

while True:

    caracter = input("Introduce un carácter: ")

    if caracter == " ":
        print("Programa cerrado.")
        break
    if caracter in "aeiou":
        print("Vocal")
    else:
        print("No vocal")