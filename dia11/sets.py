"""conjunto de datos, que no permite duplicados
no es ordenado, se escriben con {}
""" 

muchos_animales = {'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Hurón', 'Hamster', 'Erizo de Tierra'}

print(muchos_animales)
#{'Hamster', 'Perro', 'Erizo de Tierra', 'Hurón', 'Gato', 'Tortuga'}

muchos_animales.add("chancho")
print(muchos_animales) #{'Erizo de Tierra', 'Tortuga', 'Perro', 'Hurón', 'chancho', 'Hamster', 'Gato'}
#print(muchos_animales["gato"]) #TypeError: 'set' object is not subscriptable
#muchos_animales.remove("leon") #KeyError: 'leon'
print(muchos_animales)
muchos_animales.discard("leon")
print(muchos_animales)
muchos_animales.pop()#elimina un elemento al azar
print(muchos_animales) #eliminó hamster

