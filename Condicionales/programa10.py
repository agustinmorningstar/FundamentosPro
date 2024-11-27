#El director de una escuela está organizando un viaje de estudios, y requiere 
#determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de 
#viajes por el servicio. La forma de cobrar es la siguiente: 
#si son 100 alumnos o más, el costo por cada alumno es de 65 euros; 
#de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, 
#y si son menos de 30, el costo de la renta del autobús es de 4000 euros, 
#sin importar el número de alumnos. 
#Realice un programa que permita determinar el pago a la compañía de autobuses 
#y lo que debe pagar cada alumno por el viaje.
#################################################################################
# Solicitar el número de alumnos al usuario
num_alumnos = int(input("Introduce el número de alumnos que asistirán al viaje: "))

# Inicializar variables
costo_por_alumno = 0
costo_total = 0

# Determinar el costo según la cantidad de alumnos
if num_alumnos >= 100:
    costo_por_alumno = 65
    costo_total = num_alumnos * costo_por_alumno
elif 50 <= num_alumnos <= 99:
    costo_por_alumno = 70
    costo_total = num_alumnos * costo_por_alumno
elif 30 <= num_alumnos <= 49:
    costo_por_alumno = 95
    costo_total = num_alumnos * costo_por_alumno
else:
    costo_total = 4000  # Costo fijo si son menos de 30 alumnos
    costo_por_alumno = costo_total / num_alumnos  # Costo dividido entre alumnos

# Mostrar los resultados
print("\nResultados del viaje:")
print(f"Pago total a la compañía de autobuses: {costo_total:.2f} euros")
print(f"Pago por alumno: {costo_por_alumno:.2f} euros")
