
def validate(opciones, eleccion):
    # Definir validación de eleccion
    ##########################################################################
    def validate(opciones, eleccion):
     while eleccion not in opciones:
        print("Opción no válida. Por favor, ingresa una opción válida.")
        eleccion = input('Ingresa una Opción: ').lower()
    return eleccion
    
    ##########################################################################
    return eleccion


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)
    
    
