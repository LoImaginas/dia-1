# ve= corresponde a la velocidad de escape en [m/s].
#g= corresponde  la constante gravitacional en [m/s^2]
#r=corresponde al radio del planeta en [m].
#gravedad=9.8
#radio=6371
from math import pow,sqrt,ceil

#paso 1
#captura y almacenar dato ingresado por el usuario (por default el input lo almacena)

radio= input("ingresa el radio en kilometros:\n")

#paso 2
# transformar string a numero(float)

radio = float(radio) #la funcion float(), transforma un string a float
#radio = float("6371") --> radio=6371
radio = float(radio) 
#paso 3
#transformar kilometros a metros (multiplicar por 1000)
radio = radio * 1000 #radio = 6371 * 1000 = 6371000

#paso 1 para gravedad
#capturar y almacenar dato ingresado por el usuario
constante_gravitacional = input("ingrese la constante gravitacional")

#paso 2 
#transformar string a numero (float)
constante_gravitacional = float(constante_gravitacional)
#constante_gravitacional = float("9.8") --> constante_gravitacional = 9.8
#calculo formula Ve =  √2gr

multiplicacion = 2 * constante_gravitacional * radio 
velocidad_escape = sqrt(multiplicacion)
print(f"la velocidad de escape es {round(velocidad_escape,1)}[m/s]")


