"""    
El factorial se define de la siguiente forma:
𝑛! = 𝑛 ∗ 𝑛 − 1 ∗ 𝑛 − 2 ∗ . . .∗ 2 ∗ 1
En un ejemplo práctico, el factorial de 5 (5!) se calculará como:
5! = 5 ∗ 4 ∗ 3 ∗ 2 ∗ 1 = 120
Por otro lado la productoria se define como la multiplicación de elementos.
𝐴 = [3,6,4,2,8]
∏ 𝐴𝑖 = 3 ∗ 6 ∗ 4 ∗ 2 ∗ 8
Para resolver este programa se solicita lo siguiente:
● Crear un script llamado ong.py que contenga las siguientes funciones:
○ Una función que calcule el factorial.
○ Una función que calcule la productoria.
○ Una función que permita controlar los cálculos. Esta función se debe invocar
de la siguiente manera:
calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)
_ 5
www.desafiolatam.com
Se ingresarán un valor numérico como argumento con el nombre fact_i cuando se requiera
calcular un factorial, y una lista como argumento prod_i cuando se requiera calcular una
productoria. Cabe destacar que la función debe permitir ingresar estos argumentos en
cualquier orden y en cualquier cantidad. El resultado de la función se debe imprimir en pantalla
de la siguiente forma:
El factorial de 5 es 120
La productoria de [4, 6, 7, 4, 3] es 2016
El factorial de 6 es 720
"""

def factorial(numero): #Calcula el factorial de un número entero positivo
    
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

def productoria(lista): #Calcula la productoria de los elementos de una lista.
    valor = 1
    for num in lista:
        valor *= num
    return valor

def calcular(**kwargs): #Controla los cálculos de factorial y productoria según los argumentos proporcionados.
    
    for clave, valor in kwargs.items():
     if clave in "factorial":
            print(f"El factorial de {valor} es {factorial(int(valor))}")
     elif clave in "productoria":
            print(f"La productoria de {valor} es {productoria(valor)}")

calcular(factorial=5)  #El factorial de 5 es 120
calcular(productoria=[3, 6, 4, 2, 8]) #La productoria de [3, 6, 4, 2, 8] es 1152
calcular(factorial=6) #El factorial de 6 es 720

#Profe, me ayude mucho con la IA. creo que necesito reforzar mucho mas esta materia porque no me senti preparada como para completar sola esta mision.
# y eso que cuando usted lo explica en clases lo comprendo, luego cuando debo realizar sola el ejercicio me cuesta empezar y resolver. 