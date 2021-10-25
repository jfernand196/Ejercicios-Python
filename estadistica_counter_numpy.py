from collections import Counter
import numpy as np

## la clase COUNTER del modulo COLLECTION nos permite realizar conteos sobre objetos iterables, por ejemplo
## sobre cadenas de caracteres, ese conteo consiste en determinar la frecuencia de aparacion o de ocurrencia de caracterec
## en una cadena de caracteres

## ITERABLES: lista, diccionario, cadena de caracteres

## COUNTER = contar el numero de ocurrencia de cada caracter

## ejemplo con listas

lista_letras = ['t', 'u', 't', 'w', 'x', 'w', 't', 'y', 'y', 'z']
contador = Counter(lista_letras)
print("clase COUNTER = contar el numero de ocurrencia de cada caracter")
print(contador)

## ejemplo con diccionario

dict_letras = {'t':3, 'u':1, 'w':2, 'x':2, 'y':2, 'z':1}
contador = Counter(dict_letras)
print()
print("ejemplo con diccionario")
print(contador)

## otro ejemplo de COUNTER

print()
contador = Counter(t=3, u=1, w=2, x=2, y=2, z=1)
print(contador)

## ejemplo con cadena de caracteres

print()
print('ejemplo con cadena de caracteres')
cadena = 'tutwxxwtyyz'
contador = Counter(cadena)
print(contador)
print()

print(contador['t']) ## comnotacion de acceso

print(contador.most_common(3)) ## el top 3 de elementos que mas se repiten, genera 3 tuplas

print()

## diccionario = {'llave':valor, 'llave':valor}
## ciclo for para iterar diccionario u objeto COUNTER


print(contador)
for x, k in contador.most_common():
    print("llave: {} - valor: {}".format(x, k))


## crear una lista de compresion (list comprejention) con los valores de conteo

conteos = [k for x, k in contador.most_common()]
print(len(conteos))
print(conteos)


## Calcular estadisticas basicas: mediana, media, moda
## operaciopnes estadisticas
## calcular promedio de los conteos variable anterior

promedio = np.mean(conteos)
mediana = np.median(conteos)
minimo = np.min(conteos)
maximo = np.max(conteos)
print()
print("promedio: %f" %promedio)
print("mediana: %f" %mediana)
print("minimo: %f" %minimo)
print("maximo: %f" %maximo)

## Calcularemos la moda para el conjunto de conteos, nos apoyaremos en el modulo scipy: es un ecosistema
## python de codigo abierto que nos facilita realizar operaciones faciles para matematicas, ciencias,
## e ingenieria

from scipy import stats

print()
moda = stats.mode(conteos)
print(conteos)
print("moda: {}".format(moda))
## MODA: el valor que mas se repite en el arreglo o lista
print("moda: {}".format(moda.mode))

