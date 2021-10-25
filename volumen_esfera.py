# calcular el volumen de una esfera a partir del radio dado

from math import pi
global volumen
def volumen_esfera(r):
    volumen = 4/3 * pi * r ** 3
    
    return volumen
    #return print('el volumen es: {} centimetros cubicos'.format(volumen))

r = float(input('ingrese el valor del radio: '))
print(volumen_esfera(r))

