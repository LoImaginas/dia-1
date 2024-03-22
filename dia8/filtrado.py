a = [100, 200, 1000, 5000, 10000, 10, 5000]
n = len(a)
filtered_array = []
for i in range(n):
   if a[i] >= 1000:
        filtered_array.append(a[i])
print(filtered_array)

##[expresión1 if condición1 else expresión2 for variable in iterable]
#siguiendo la logica 

filtered_array2 =[a[i] for i in range(n) if a[i] >= 1000 ] #se utiliza la tercera expresion de comprehesion
#si el if esta antes del for, DEBE haber un else
#si solo hau 1 if, va despues de for in range(n)


print(filtered_array2)

