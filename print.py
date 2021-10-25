# Comando print
# END=
print('ejemplo de texto', end='')
print('ejemplo 2 de texto')
# OUTPUT ejemplo de textoejemplo 2 de texto
print()
#SEP=
print('ejemplo', '2', 'de texto')
print('ejemplo', '2', 'de texto', sep='-')
# OUTPUT ejemplo-2-de texto
print()
#OUTPUT PLACEHOLDER
print('{} 2 de {}'.format('ejemplo', 'de texto'))
#OUTPUT ejemplo 2 de de texto
print()
#LISTA
numeros = [2,3,4,5,7]
print(numeros)
#OUTPUT [2, 3, 4, 5, 7]
print()
#DICCIONARIOS
capitales = {'Colombia':'Bogota', 'Peru':'Lima'}
print(capitales)
#OUTPUT {'Colombia': 'Bogota', 'Peru': 'Lima'}
