suma = 0
cn = 0

print("Ingresa 10 números:")
for i in range(10):
    numero = float(input(f"Ingrese el número {i + 1}:"))
    suma += numero
    cn += 1
promedio = suma/cn

print(f"El promedio de los números ingresados es: {promedio}")