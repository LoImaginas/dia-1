import sys,random

numero_buscar = int(sys.argv[1]) #numero a buscar

lista =[1,2,3,4,5,6,7,8,9,0]
random.shuffle(lista) #desordenar la lista
print(lista)

for posicion, numero in enumerate(lista):
    
    if numero_buscar == numero:
        print("Numero encontrado")
        break
    else:
        print(f"El numero no se encuentra en la posicion{posicion}\n")
    
print("fuera del for")
print(f"El numero{numero_buscar} se encontro en la posicion{posicion}")    