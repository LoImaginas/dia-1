"""
La empresa tiene un contrato con una tienda de tecnología en la cual quieren implementar un
filtrado por precio. Para ello se solicita generar el archivo filtro.py con la solución al
problema. Dada una muestra de los productos que actualmente se encuentran disponibles en
la tienda (un diccionario), se solicita implementar una función que permita entregar lo
siguiente:
● Un diccionario con los productos que cumplen una cierta condición dado un umbral
● La función debe permitir mostrar los valores mayor que o menor que un umbral
(siempre estrictos).
● Por defecto la función debe siempre mostrar los valores mayor que el umbral a menos
que se indique lo contrario.
"""

import sys

precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

#filtrar

def filtrar_por_precio(precios, umbral, condicion='mayor'):
    
    #Filtra los productos según un umbral dado y una comparación especificada.
    
    if condicion == 'menor':
        productos_filtrados = {producto: precio for producto, precio in precios.items() if precio < umbral}
    elif condicion == 'mayor':
        productos_filtrados = {producto: precio for producto, precio in precios.items() if precio > umbral}
    else:
        return "Lo sentimos, no es una operación válida"
    
    return productos_filtrados


#aplicar metodo

if len(sys.argv) == 2:
        umbral = int(sys.argv[1])
        resultado = filtrar_por_precio(precios, umbral)
        if type(resultado)==dict:
           print("Los productos mayores al umbral son:", ', '.join(resultado.keys()))
        else:
            print(resultado) 
elif len(sys.argv) == 3:
        umbral = int(sys.argv[1])
        condicion = sys.argv[2].lower()
        resultado = filtrar_por_precio(precios, umbral, condicion)
        if type(resultado)==dict:
            print("Los productos", condicion, "al umbral son:", ', '.join(resultado.keys()))
        else:
            print(resultado)
else:
        print("Uso: python3 dia13_desafio4/filtro.py <umbral> [mayor|menor]")
        
        #python3 dia13_desafio4/filtro.py 30000  Los productos mayores al umbral son: Notebook, Monitor, Escritorio, Tarjeta de Video
        #python3 dia13_desafio4/filtro.py 30000 menor Los productos menor al umbral son: Teclado, Mouse
        #python3 dia13_desafio4/filtro.py 30000 otro Lo sentimos, no es una operación válida
        