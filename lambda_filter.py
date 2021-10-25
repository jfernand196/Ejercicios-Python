# obtener los numeros divisibles por 7 unasndo funcion anonima

numeros = [3, 14, 29, 42, 70, 2, 7, 8, 9, 13]

divisibre_por_7 = lambda x : x % 7 == 0

num_div_7 = filter(divisibre_por_7, numeros)

print(list(num_div_7))

# usar filter para obtener los numeros positivos de una lista

numeros2 = [-1, 2, 3, -6, -7]

# mayores_cero = list(filter(lambda x: x>0, numeros2)) 
print(list(filter(lambda x: x>0, numeros2)))


from functools import reduce

print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))

from itertools import accumulate

print(list(accumulate([1, 2, 3, 4, 5])))

