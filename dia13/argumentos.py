def f(*parametros):  #tuplas #def funcion_tuplas(*parametros):
    print(parametros) 
    return parametros

output = f(1,[2,3],'hola',{'clave':[4]}) #(1, [2, 3], 'hola', {'clave': [4]})
print(type(output)) #<class 'tuple'>


def f(**parametros): #def funcion_dicc(**parametros):
    print(parametros) #{'valor': 1, 'texto': 'hola', 'lista_nombres': [4, 5, 6, 7]}
    return parametros

output = f(valor = 1, texto = 'hola', lista_nombres= [4,5,6,7])
print(type(output))