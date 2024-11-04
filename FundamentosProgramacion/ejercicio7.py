# 7. Convertir minutos a horas y minutos
minutos = int(input("Ingrese la cantidad de minutos: "))
horas = minutos // 60
min_restantes = minutos % 60
print(horas, "horas y", min_restantes, "minutos")