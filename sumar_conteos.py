# computar la suma de los conteos de los duplicados de una lista

from collections import Counter

numeros = [2,3,4,5,2,2,3,7,8,8]

conteos = Counter(numeros)

print(conteos)

print(sum(conteos.values()))
print(sum(conteos))