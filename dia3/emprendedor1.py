#Utilidades = Precio * Usuarios - Gasto total
#PRECIO DE SUSCRIPCION
#NUMERO DE USUARIOS
#GASTOS TOTALES
from math import pow,sqrt,ceil

precio = input("ingresa el precio de suscripcion:\n") #100
precio = int(precio)

usuarios = input("ingresa el numero de usuarios:\n") #10
usuarios = int(usuarios)

gasto_total = input("ingresa el gasto total:\n") #50
gasto_total = int(gasto_total)

utilidades = precio * usuarios - gasto_total #utilidades=100*10-50
print(f"las utilidades son (utilidades) pesos")#950




