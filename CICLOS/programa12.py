'''
Realizar un programa para determinar cuánto ahorrará una persona en un año, 
si al final de cada mes deposita cantidades variables de dinero; 
además, se quiere saber cuánto lleva ahorrado cada mes.
'''
total_ahorrado = 0

for mes in range(1, 13):
    deposito = float(input(f"Introduce la cantidad a ahorrar en el mes {mes}: "))
    total_ahorrado += deposito
    print(f"Total ahorrado hasta el mes {mes}: ${total_ahorrado:.2f}")
    
print(f"\nEl total ahorrado en el año es: ${total_ahorrado:.2f}")
