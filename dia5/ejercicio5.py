edad = 27

#¿Juan es mayor de edad?
print(edad>=18) #true
print(edad < 18) #false

#juan se graduo del colegio antes de los 18?
edad_graduacion_colegio = 17
print(edad_graduacion_colegio < 18) #true
print(edad_graduacion_colegio ==18) #false
print(edad_graduacion_colegio > 18) #false
print(edad_graduacion_colegio >=18) #false --> mayor 0 Igual

#¿juan No tiene 4 años de experiencia laboral?
experiencia_laboral = 4
print(experiencia_laboral !=4) #false
print(experiencia_laboral == 4) #true
print(experiencia_laboral < 4) #false  (por si solo no funciona respondiendo la pregunta)
print(experiencia_laboral < 4 or experiencia_laboral > 4)#con(and) es false  - con (or) es false

#Juan Tiene hijos?
numero_hijos=0
print(numero_hijos > 0) #false
print(numero_hijos < 1) #true
print(numero_hijos == 0) #true
print(numero_hijos !=0) #false

nombre = "Lolett"
#comparacion entre = y ==
me_llamo_juan = nombre == "juan"
me_llamo_juan #false

nombre = "juan"
me_llamo_juan = nombre == "juan"
me_llamo_juan #true
#lo que se evalua es siempre lo que esta a la derecha del =
#resuelve la parte derecha del = 

""" edad > 18 y duracion_pololeo > 0
 
P = edad > 18
Q = duracion_pololeo > 0 


p = T ; p = F
q = T ; q = F
r = T ; r = F 

cantidad de combinaciones
2^2=4
2^3=8

  y (and) --> se deben cumplir ambas condiciones
  SI AMBAS SON VERDADERAS, EL RESULTADO ES VERDADERO (TRUE)

P  Q  and 
V  V = V *
V  F = F 
F  V = F
F  F = F 
-------------------------------------------------
  o (or) --> se debe cumplir una de las condiciones
  SI AMBOS SON FALSOS, TODO EL RESULTADO ES FALSO (FALSE)

P  Q  or 
V  V = V 
V  F = V 
F  V = V
F  F = F *

"""

#soy estudiante y ingreso a clases todos los dias
"""
P = SOY_ESTUDIANTE
Q = INGRESO_A_CLASES_TODOS_LOS_DIAS

P  Q   and 
V  V =  V
V  F =  F
F  V =  F
F  F =  F

P (v) Q (f) = FALSE

#me gusta comer frutas o comer verduras 
P = ME_GUSTA_COMER_FRUTAS
Q = ME_GUSTA_COMER_VERDURAS

P  Q  or 
V  V =  V
V  F =  V
F  V =  V
F  F =  F

P (v) Q (v) = TRUE

+ * + = +
+ * - = -
- * + = -
- * - = + 


ser o no ser 


"""