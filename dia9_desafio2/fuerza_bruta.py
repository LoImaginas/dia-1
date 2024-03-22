#Actividad 3 - Fuerza bruta

import getpass
from string import ascii_lowercase #es un string con todas las letras del abecedario en minúsculas (sin la ñ).

password = getpass.getpass("Ingresa la contraseña:").lower()
#password = input("Ingresa la contraseña:").lower() #gato

minusculas = ascii_lowercase 
print(minusculas)
contador = 0

for caracter in password:
    print(caracter)
    for letra in minusculas:
        contador+=1
        if caracter == letra: 
            break

print(f"La contraseña fue forzada en {contador} intentos") #Se considera "intento" cada vez que se compara una letra.
