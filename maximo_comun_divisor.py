## calcular el maximo comun divisor de dos numeros
#reglas:

"""                  Algoritmo de Euclides

El algoritmo de Euclides es un conocido algoritmo para calcular el máximo común divisor de dos números. 
Se basa en la siguiente propiedad: mcd(a,b)=mcd(a−b,b). Así, si se va sustrayendo el número menor 
de el número mayor, cada vez los pares de números que quedan se van haciendo más pequeños hasta que 
uno de los números es 0, y mcd(a,0)=a. 

Por ejemplo, para calcular el máximo común divisor de 105 y 70:

mcd(105,70)=mcd(105−70,70)=mcd(35,70)=mcd(35,70−35)=mcd(35,35)=mcd(35,35−35)=mcd(35,0)=35 """

# x = int(input('introdusca el primer numero: '))
# y = int(input('introdusca el segundo numero: '))

# import math

# def mcd(x,y):
#     num_mayor = max(x, y)
#     num_menor = min(x, y)
#     # print(num_mayor)
#     # print(num_menor)
#     diferencia = num_mayor - num_menor
#     while diferencia !=0:
#         num_mayor = diferencia
#         diferencia = abs(num_mayor - num_menor)
#         num_menor = num_mayor
#     return num_mayor

# print('el mcd entre {} y {} es: {}'.format(x, y, mcd(x,y)))

#segunda forma

from math import gcd

x = int(input('introdusca el primer numero: '))
y = int(input('introdusca el segundo numero: '))

print(gcd(x,y))



