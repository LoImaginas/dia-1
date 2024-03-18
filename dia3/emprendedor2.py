#Utilidades = Precio * Usuarios - Gasto total
#PRECIO DE SUSCRIPCION
#NUMERO DE USUARIOS
#GASTOS TOTALES
from math import pow,sqrt,ceil

precio = input("ingresa el precio de suscripcion:\n") #100
precio = float(precio)

usuarios_normales = input("ingresa el numero de usuarios normales:\n") #7
usuarios_normales= int(usuarios_normales)

usuarios_premium = input("ingresa el numero de usuarios premium:\n") #3
usuarios_premium = int(usuarios_premium)

gasto_total = input("ingresa el gasto total:\n") #50
gasto_total = float(gasto_total)

utilidades = (precio * usuarios_normales) + ((precio * 1.5) * usuarios_premium) - gasto_total #utilidades = (100 * 7) + ((100 * 1.5) * 3) - 50
print(f"las utilidades son (utilidades) pesos")# 1100

