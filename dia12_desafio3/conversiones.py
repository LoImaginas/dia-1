"""
Grupo1:
Felipe Arias
Najla Gatica
Lolett Llanquinao
Jimena Traipe
"""

#Desafío - Estructuras de datos y funciones (I)
#Actividad 1

import sys
# Paso 2: Obtener las tasas de conversión y el valor en pesos chilenos desde sys.argv

# Paso 3: Calcular el equivalente en las tres monedas y mostrar el resultado
sol_peruano = float(sys.argv[1]) #ubicación 1
peso_argentino = float(sys.argv[2]) #ubicación 2
dolar_americano = float(sys.argv[3]) #ubicación 3
peso_chileno = int(sys.argv[4]) #ubicacion 4

#imprimir resultados: 
print(f"Tasa a sol peruano {sol_peruano}")
print(f"Tasa a peso argentino {peso_argentino}")
print(f"Tasa a dolar americano {dolar_americano}")


#convertir los clp a otras divisas
conversion_sp = (sol_peruano * peso_chileno)
conversion_pa = (peso_argentino * peso_chileno)
conversion_da = (dolar_americano * peso_chileno)


#imprimir los resultados
print(f"Los {peso_chileno} pesos equivalen a:")
print(f"{conversion_sp} sol peruano")
print(f"{conversion_pa} pesos argentinos")
print(f"{conversion_da} dolar americano")

#python3 dia12_desafio3/conversiones.py 0.0046 0.093 0.0013 10000