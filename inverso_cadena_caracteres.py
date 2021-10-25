# Obtener la representacion inversa de una cadena de caracteres

#Python => nohtyP

cadena = 'Python'

#OPCION 1
for i in range(len(cadena) -1, -1, -1):
    print(cadena[i], end='')

#OPCION 2 WITH SLICE
print()
print(cadena[::-1])