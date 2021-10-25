# generar combinaciones atraves del modulo itertools

from itertools import combinations

numeros = [3,4,5,1,2,7,8]
cont = 0

for i in combinations(numeros, 3):
    cont +=1
    print(cont,'.', i)

