# Duplica cada elemento
# Escribe una función llamada duplicar que reciba un arreglo de números como parámetro y retorne un 
# nuevo arreglo con cada elemento duplicado (multiplicado por dos).

# duplicar([3, 12, 45, 7]) # retorna [6, 24, 90, 14]
# duplicar([8, 5]) # retorna [16, 10]

def duplicar(x):
    return [i*2 for i in x]

print(duplicar([3, 12, 45, 7]))
print(duplicar([8, 5]))