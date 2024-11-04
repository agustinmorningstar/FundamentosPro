# 12. Distancia entre dos puntos en el plano
import math
x1 = float(input("Ingrese la coordenada x1: "))
y1 = float(input("Ingrese la coordenada y1: "))
x2 = float(input("Ingrese la coordenada x2: "))
y2 = float(input("Ingrese la coordenada y2: "))
distancia =math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("La distancia entre los puntos es:", distancia)
