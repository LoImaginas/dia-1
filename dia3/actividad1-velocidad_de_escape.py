# ve= corresponde a la velocidad de escape en [m/s].
#g= corresponde  la constante gravitacional en [m/s^2]
#r=corresponde al radio del planeta en [m].
g=9.8
r=6371
from math import pow,sqrt,ceil

input("ingresa el radio en kilometros:\n")
print(f"el radio es {r}")
input("ingresa la constante g:\n")
print(f"la constante g es {g}")
print(sqrt(2*(g*r)))
