PI=3,14
IVA = 19


suma=4 #variable global

def sumar(numero1,numero2):
    #variable local 
    #global suma
    suma = numero1 + numero2
    return suma #retur 33
    # return numero1+numero2 #suma #return 33                #con el return

#llamado a la funcion                                      #o no hago nada  
sumar(14,15)                  

#imprimir el valor de retorno al llamar a la funcion       # o lo imprimo
print(sumar(15,16)) #31 

#captura el valor de retorno al llamar a la funcion        #o lo capturo 
 
valor_retorno = sumar(16,17)
print(valor_retorno) #33

print(suma)