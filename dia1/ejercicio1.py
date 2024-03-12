print("texto a imprimir en consola")
print (2+2)
numero = 23
print(numero)

#limitantes
#no esta permitido la suma de latras y numros
# print("texto"+12) #TypeError: can only concatenate str (not "int" to string )
print("texto",12)
#concatenar = "texto"+12
print("texto"+"34")

#INTERPOLACION
print(f"el numero es {numero+2}")
nombre = "Luna"
print(f"Tu nombre es {nombre} \n y tu edad es {numero}")
print("Tu nombre es "+nombre)
#string.format
print("Tu nombre es {} y tu edad es {}".format(nombre,numero))
# formato con %
print("Tu nombre es %s y tu edad es %d" % (nombre,numero))
#metodo con cadena
apellido = "llanquinao peso"
print(apellido.title())
# dato importante 
# >>> (esto significa que se ha creado una nueva terminal)