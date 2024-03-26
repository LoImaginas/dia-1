"""
Diccionarios {}

estructura datos de pares clave:valor
se accede a los elementos a traves de la clave, no importa la posición
las claves no se generan automaticamente, no hay un orden
las claves pueden ser String, numerico, incluso Boolean
los valores pueden ser: String, numerico, boolean, listas, diccionario u otro tipo de datos
Si la clave existe,modifico su valor, si no existe se agrega el par clave:valor

"""


diccionario = {
    1: "uno",
    "dos": 2,
    3: ["a","b","c"], # lista dentro de diccionario
    "dicc": {"A":"A Mayuscula"},
    }

#Diccionario vacio
notas={}

notas = {
"Camila": 7,
"Antonio": 5,
"Felipe": 6,
"Daniela": 5,
"Vicente": 7,
"Vicente":1
}
print(len(notas)) #5
print(notas) #{'Camila': 7, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 7}

#Acceso a los elementos(valores)
print(notas["Camila"])#7
print(notas["Antonio"])#5
print(notas["Felipe"])#6
print(notas["Daniela"])#5
print(notas["Vicente"])#7
#print(notas["Vicente"])#1 se sobrescribe, 1 reemplaza a 7 si hay dos notas iguales.
#print(notas["camila"])#KeyError: 'camila'
print(notas)#{'Camila': 7, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 1, 'FELIPE': 2}

#agregar 
notas["Lolett"] = 4
print(notas)#{'Camila': 7, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 1, 'FELIPE': 2, 'Lolett': 4}


#Modificar par clave:valor
notas["Lolett"] = 5
print(notas)#

#eliminar par clave:valor

#1 forma 
"""del notas["FELIPE"]"""
print(notas)#{'Camila': 7, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 1, 'Lolett': 5}

#2 forma pop()-> al eliminar, capturamos el valor
eliminado = notas.pop("Camila") #notas["Camila"]
print("valor eliminado : ",eliminado)#7
print(notas)#{'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 1, 'Lolett': 5}
print("")
notas2 = {
    "Marcela":2,
    "Ana":1,
    "Felipe": 7,
    }

#notas.update(notas2)
#print(notas)#
notas2.update(notas)
print(notas2)#{'Marcela': 2, 'Ana': 1, 'Felipe': 6, 'Antonio': 5, 'Daniela': 5, 'Vicente': 1, 'Lolett': 5}

#COLISIONES: al existir duplicidad de claves, se conserva el valor del dicionario anexado