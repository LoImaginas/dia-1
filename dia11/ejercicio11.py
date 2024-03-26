#crear un diccionario

gatitos = {
"Gato_Andino": "en peligro de extinción", 
"Gato_Guiña": "vulnerable",
"Gato_Geoffroy": "casi amenazado",
"Gato_Colocolo": "casi amenazado",
}

print(gatitos) #{'Gato_Andino': 'en peligro de extinción', 'Gato_Guiña': 'vulnerable', 'Gato_Geoffroy': 'casi amenazado', 'Gato_Colocolo': 'casi amenazado'}

#agregar un elemento 

gatitos["Puma"]= "preocupación menor"
print(gatitos)#{'Gato_Andino': 'en peligro de extinción', 'Gato_Guiña': 'vulnerable', 'Gato_Geoffroy': 'casi amenazado', 'Gato_Colocolo': 'casi amenazado', 'Puma': 'preocupación menor',}

#cambia un elemento 
gatitos["Gato_Geoffroy"]= "en peligro de extinción"
print(gatitos) #{'Gato_Andino': 'en peligro de extinción', 'Gato_Guiña': 'vulnerable', 'Gato_Geoffroy': 'en peligro de extinción', 'Gato_Colocolo': 'casi amenazado', 'Puma': 'preocupación menor'}

#elimina un elemento
eliminado = gatitos.pop("Puma")
print("valor eliminado : ",eliminado) #valor eliminado :  preocupación menor
print(gatitos) #{'Gato_Andino': 'en peligro de extinción', 'Gato_Guiña': 'vulnerable', 'Gato_Geoffroy': 'en peligro de extinción', 'Gato_Colocolo': 'casi amenazado'}