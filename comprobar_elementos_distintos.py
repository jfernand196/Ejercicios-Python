#Comprobar si todos los elementos de una lista son distintos.

def elementos_distintos(datos):
    return len(datos) == len(set(datos))

print(elementos_distintos([1,2,2,3,4,5]))
print(elementos_distintos([1,2,3,4,5,6]))