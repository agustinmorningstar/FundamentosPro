'''
Mostrar en pantalla los N primero números primos. Se pide por teclado la cantidad 
de números primos que queremos mostrar.
'''
n = int(input("¿Cuántos números primos deseas mostrar? "))

contador = 0
numero = 2

print(f"Los primeros {n} números primos son:")

while contador < n:
    es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print(numero, end=" ")
        contador += 1
    numero += 1
