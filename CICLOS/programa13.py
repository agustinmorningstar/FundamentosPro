'''
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 
euros, el segundo 20 euros, el tercero 30 euros y así sucesivamente. 
Realizar un programa para determinar cuánto debe pagar mensualmente y el total 
de lo que pagó después de los 20 meses.
'''
total_pagado = 0

for mes in range(1, 21):
    pago_mensual = mes * 10
    total_pagado += pago_mensual
    print(f"Mes {mes}: Pago mensual = {pago_mensual} euros")
print(f"Total pagado después de 20 meses: {total_pagado} euros")
