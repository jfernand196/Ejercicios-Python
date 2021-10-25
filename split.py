

from typing import Reversible


x = 'aWESOME is cODING'
print(x)
minuscula = 'abcdefghijklmnñopqrstwxyz'
mayuscula = 'ABCDEFGHIJKLMNÑOPQRSTWXYZ'
y = x.split()
print(y)
palabra = ''
for i in x:
    if i in minuscula:
        palabra += i.upper()
    if i in mayuscula:
        palabra += i.lower()
    if i == ' ':
        palabra += i

print(palabra)    
g = palabra.split()
print(g)

rev1 = str(palabra)
print(rev1)
#for k in range(len(rev1)):
#    rev = print(rev1[k], end=" ")
#print(rev)