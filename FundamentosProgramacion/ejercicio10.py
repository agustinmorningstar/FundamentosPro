# 10. Calificación final
c1= float(input("Ingrese el promedio de primer parcial: "))
c2= float(input("Ingrese el promedio de segundo parcial: "))
c3= float(input("Ingrese el promedio de tercer parcial: "))
promedio_parciales = (c1+c2+c3)/3
examen_final = float(input("Ingrese la calificación del examen final: "))
trabajo_final = float(input("Ingrese la calificación del trabajo final: "))
calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)
print("Calificación final:", calificacion_final)
