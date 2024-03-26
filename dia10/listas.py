"""
LISTAS 
[] --> listas
()--> tuplas
{} --> diccionarios
Son contenedores de datos
son mutable
conjunto de datos, separados por coma, ordenando segun su ingreso
la primera posicion (INDICE) es cero
"""

lista_pares=[2,4,6,8,10]
#tamño de la lista es 5
print(lista_pares)
print(len(lista_pares))#imprime el tamaño
print[2,4,6,8,10]

#indice o posicion

print(lista_pares[0]) #2
print(lista_pares[1]) #4
print(lista_pares[2]) #6
print(lista_pares[3]) #8
print(lista_pares[4]) #10
#print(lista_pares[5]) #error indexError: list index out of range
print("")
print(lista_pares[-1])#10
print(lista_pares[-2])#8


lista_vacia=[]#tamaño es cero

# https://docs.python.org/es/3/tutorial/datastructures.html

#METODOS (listas_pares.)
print(lista_pares.__dir__) #<built-in method __dir__ of list object at 0x1013b6b00>
print(lista_pares.__dir__())#<built-in method __dir__ of list object at 0x100c35b00>['__repr__', '__hash__', '__getattribute__', '__lt__', '_

#append(dato)=> lo que haces es agregar un elemnto al final de la lista
lista_vacia.append("lunes")
lista_pares.append(13)
print(lista_vacia)
lista_vacia.append("martes")
lista_vacia.append("miercoles")
print(lista_vacia)

#insert(indice,elemento) => inserta un elemento en una posicion especifica, no reemplaza
lista_vacia.insert(3,"jueves")
print(lista_vacia) #['lunes', 'martes', 'miercoles', 'jueves']
lista_vacia.insert(3,"viernes")
print(lista_vacia) #['lunes', 'martes', 'miercoles', 'viernes', 'jueves']
#reemplaza
lista_vacia[3]="Jueves"#reemplazar el elemento en esa posicion
#lista_vacia[6]="Jueves" #IndexError: list assignment index out of range
print(lista_vacia)#['lunes', 'martes', 'miercoles', 'Jueves', 'jueves']
lista_vacia.insert(10,"Sabado")
print(lista_vacia)#['lunes', 'martes', 'miercoles', 'Jueves', 'jueves', 'Sabado']


#pop()=> saca el ultimo elemento dentro de la lista, si no se pasa un indice
lista_vacia.pop()
print(lista_vacia)#['lunes', 'martes', 'miercoles', 'Jueves', 'jueves']

lista_vacia.pop(4) 
print(lista_vacia)#['lunes', 'martes', 'miercoles', 'jueves']

lista_eliminados = []

lista_eliminados.append(lista_vacia.pop(0))

Eliminado=lista_vacia.pop(0) 

lista_eliminados.append(Eliminado)

#print(f"el elemento eliminado {Eliminado}") #el elemento eliminado martes
print(lista_vacia) #['miercoles', 'Jueves']
print(lista_eliminados) #'lunes', 'martes']

#remove(valor) => elimina un valor
lista_vacia.remove("miercoles")
print(lista_vacia) #jueves
#lista_vacia.remove("lunes")#ValueError: list.remove(x): x not in list

lista_vacia.append("lunes")
print(lista_vacia) #['Jueves', 'lunes']
lista_vacia.append("lunes")
print(lista_vacia)

lista_vacia.remove("lunes") #elimina la primera coicidencia, de izquierda a derecha
print(lista_vacia) #['Jueves', 'lunes']

lista_vacia.insert(0,"Martes")
lista_vacia.insert(0,"miercoles")
lista_vacia.append("viernes")
lista_vacia.append("sabado")
lista_vacia.append("domingo")
print(lista_vacia) 



#reverse()=> invierte los elementos de la lista, el cambio es permanente
lista_vacia.reverse()
print(lista_vacia) #['lunes', 'Jueves']"""

#sort()=> Ordena los elementos de forma ascendente/alfabaticamente
lista_vacia.sort()
print(lista_vacia)#['Domingo', 'Jueves', 'Lunes', 'Martes', 'Miercoles', 'Sabado', 'Viernes']

lista_pares.sort()
print(lista_pares)#[2, 4, 6, 8, 10, 13]
print(lista_vacia)#

#respaldo de lista
lista1=lista_pares#[2, 4, 6, 8, 10, 13] lista_pares#[2, 4, 6, 8, 10, 13]

lista2=lista_pares.copy() #si es un respaldo de la lista original
lista3=lista_pares[:]     #si es un respaldo de la lista original
lista4=lista_pares + []   #si es un respaldo de la lista original
lista5=lista_pares * 1    #si es un respaldo de la lista original
lista6= list(lista_pares) #si es un respaldo de la lista original



lista_pares.pop()
print("lista de pares",lista_pares)
print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)
print(lista6)

#sorted(lista, reverse=true), ordena descendentemente, pero no es permanente.
sorted(lista_pares, reverse= True)#ordena desc
print(sorted(lista_pares, reverse= True)) #10,8,6,4,2  
print(lista_pares)#[2,4,6,8,10]

#index() => retorna el indice del elemento que se busca en una lista

print("indice del elemento 8 es:", lista_pares.index(8))
#print("indice del elemento 13 es :", lista_pares.index(13)) #ValueError:13 is not in list

sorted(lista_pares, reverse= True)#ordena desc
sorted(lista_pares)#ordena asc
sorted(lista_pares, reverse= False)#ordena asc

lista_final = lista_pares + lista_vacia
print("lista final",lista_final)