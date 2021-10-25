# Cuenta los asteriscos
# Escribe una función llamada asteriscos que reciba un string str y retorne el número de asteriscos 
# que hay en str.

# asteriscos("H*o*l*a") # retorna 3
# asteriscos("Hola") # retorna 0

# Opcion 1

# def asteriscos(x):
#     cont = 0
#     for i in x:
#         if i == '*':
#             cont += 1
#     return cont

# Opcion 2
def asteriscos(x):
    return len([i for i in x if i == '*'])

print(asteriscos("H*o*l*a"))
print(asteriscos("Hola"))