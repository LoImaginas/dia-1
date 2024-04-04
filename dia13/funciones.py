def imprimir_menu():
    print('Opciones: ')
    print('1) De acuerdo')
    print('2) En desacuerdo')
    print('3) No me interesa')
 
def imprimir_respuestas():
    
    
    """
    print(f'la respuesta a la pregunta 1 fue {respuestas[0]}')
    print(f'la respuesta a la pregunta 2 fue {respuestas[1]}')
    print(f'la respuesta a la pregunta 3 fue {respuestas[2]}')
    #for i in range(3): #el rango de 0 a 2 
    """ 
    """  
    for i in range (len(respuestas))  #cuando no se el rango, se llaman todas las respuestas        
        print(f'la respuesta a la pregunta {i+1} fue {respuestas[i]}')
    """  
    for posicion, respuesta in enumerate(respuestas): 
       print(f'la respuesta a la pregunta{posicion+1} fue {respuesta}')   
        
preguntas = ['enunciado pregunta 1','enunciado pregunta 2', 'enunciado pregunta 3']
respuestas = [] 

#hacer preguntas 
for pregunta in preguntas:
    print(pregunta)
   #llamado o invocacion  
    imprimir_menu()
    respuestas.append(input('>'))
    print("")
    
    
print("")
#llamado o invocacion a la funcion
imprimir_respuestas()
    



