#################################################################################
#Programa que pida tres números y los muestre ordenados (de mayor a menor);
#################################################################################

n1=int(input("escribe el numero 1 :"))
n2=int(input("escribe el numero 2 :"))
n3=int(input("escribe el numero 3 :"))
if n1 > n2 and n2 < n3 :
     print(f"el orden de mayor a menor es {n1} , {n2} , {n3}" )
else: 
   print("error")
   