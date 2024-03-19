#crear un scrip de ingreso de password
#donde el largo minimo es 6 caracteres
import getpass
password=input("ingrese su contraseña:")
password = getpass.getpass("ingrese su cotraseña:")

if password == "12345":
    print("El password es incorrecto")

if len(password)<6:
    print("el password es demasiado corto")