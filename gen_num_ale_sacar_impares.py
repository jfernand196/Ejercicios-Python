## generar n cantidad de numeros aleatorios e identificar los numeros impares

from random import randint



def num_impares(n=5):
    impares = []
    while True:
        numeros = [randint(1, 10) for _ in range(n)]
        
        if all(x % 2 == 1 for x in numeros):
            impares = numeros
            break

    return impares

impares = num_impares()
print(impares)
print(num_impares(20))

