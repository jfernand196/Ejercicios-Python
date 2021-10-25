#Crear un histograma a partir de una lista de enteros
'''
def histograma_enteros(lista):
    ast = ''
    ast1 = '*'

    for i in lista:
        for e in range(i+1):
            ast += ast1  
        print ast  
'''

'''
for i in [9, 4, 6, 1, 12]:
    ast1 = '*'
    ast = ''
    for e in range(i):
        ast += ast1
    print(ast)
'''

## opcion 1
def hist_ent(lista):
    
    for i in lista:
        ast1 = '*'
        ast = ''
        fin=''
        for e in range(i):
            ast += ast1   
        print(ast)
    

hist_ent([2,4,6,7])
print()
print()

## opcion 2
def hist_ent(lista, caracter='*'):
    
    for i in lista:
     print(caracter * i)


print()
print()
hist_ent([2,4,6,7])
print()
print()

## Danny---
def my_function(food):
  for x in food:
    caractera = ""
    for y in range(x):   
        caractera = caractera + "*"
    print(caractera)
 
my_function([5, 2, 3])

print()
print()
print('*' * 3)