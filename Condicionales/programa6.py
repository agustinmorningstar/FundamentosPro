#################################################################################
# Realiza un programa que calcule la potencia, para ello pide por teclado 
# la base y el exponente. Pueden ocurrir tres cosas:
# * El exponente sea positivo, sólo tienes que imprimir la potencia.
# * El exponente sea 0, el resultado es 1.
# * El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
#################################################################################
import math
base=int(input("Escribe el numero base : "))
potencia=int(input("Escribe la potencia a elevar la base :"))
if potencia > 0 :
    total=base**potencia
    print(f"La potencia de {base} a la {potencia} es igual a : {total}")
else:
    if potencia==0 :
        print(f"La potencia de cualquier numero a la exponente {potencia} es igual a 1")
    else: 
        if potencia < 0 :
                total=1/base**potencia
        else:
            print("error debes ingresar un numero")

                
