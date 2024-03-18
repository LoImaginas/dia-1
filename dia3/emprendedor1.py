#Utilidades = P * U - GT
#P = PRECIO DE SUSCRIPCION
#U = NUMERO DE USUARIOS
#GT= GASTOS TOTALES
from math import pow,sqrt,ceil

input("ingresa el precio de suscripcion:\n")
p = 50
print(f"el precio de suscripcion es {p}")

input("ingresa el numero de usuarios:\n")
u= 150
print(f"el numero de usuarios es {u}")

input("ingresa el gasto total:\n")
gt=1320
print(f"el gasto total es {gt}")

print(sqrt(p*u-gt))
Utilidad=78.61



