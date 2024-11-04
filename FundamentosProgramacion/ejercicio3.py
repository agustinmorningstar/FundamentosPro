# 3. Calcular la hipotenusa de un triángulo rectángulo
import math
cateto1 = float(input("Ingrese el primer cateto: "))
cateto2 = float(input("Ingrese el segundo cateto: "))
h = math.sqrt(cateto1**2 + cateto2**2)
print("La hipotenusa es:", h)