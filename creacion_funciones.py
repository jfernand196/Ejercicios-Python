## creacion de funciones

# definicion de variable global

i = 40
def newfunc():
    i = 90
    return i
print()
print(newfunc()) # imprime la variable i creda dentro de la funcion
print(i) # imprime la variable i creada de forma global

# Otra forma de declarar variables globales

def newfunc():
    global f
    f = 90
    return f
print()
print(newfunc()) # imprime la variable i creda dentro de la funcion
print(f) # imprime la variable i creada de forma global