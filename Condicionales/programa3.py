## Crea un programa que pida al usuario dos números y muestre su división 
##si el segundo no es cero, o un mensaje de aviso en caso contrario
dividendo=int(input("Escribe el primer numero"))
divisor=int(input("Escribe el segundo numero"))
if divisor == 0 :
    print(f"El divisor no puede ser {divisor}")
else:
    division=dividendo/divisor
    print(f"la division de {dividendo} entre {divisor} es igual a : {division}")
    


