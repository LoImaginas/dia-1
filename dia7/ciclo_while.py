"""
    while condicion:
    #codigo a ejecutar
    
"""
#import getpass

password = input("ingrese su contraseña:\n")

while password != "hola mundo":
    password = input("contraseña incorrecta, Ingrese su contraseña")

print("\n contraseña correcta!")
#resto del programa

#print(fin del programa)    
    
#metodo Len 
password = input("ingrese su contraseña:\n")

while len(password) < 6:
    password = input("ingrese su contraseña con largo superior o igual a 6 caracteres:\n ")
    
while password != "hola mundo":
    password = input("contraseña incorrecta, Ingrese su contraseña")
    
#Iteracion de n veces
i = 0 
while i < 10:
    print(f"El valor de i es:{i}")
    i+=2 #i = i + 1 #incremento en 1

print(f"fuera de while, valor de i= {i}")  
    
"""
while True:
    print("acciones infinitas")
    if condicion:
    else:
        break #salir del bucle
"""

saludo = "Hola"
saludo = saludo + " Mundo"
print(saludo)
saludo += "chao"
print(saludo)