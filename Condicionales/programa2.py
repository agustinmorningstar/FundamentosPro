# Escribe un programa que lea un número e indique si es par o impar.
numero=int(input("Escribe el numero : "))
mod=numero%2
if mod == 0:
    print(f"el numero {numero} es par")
else:
     print(f"el numero {numero} es impar")