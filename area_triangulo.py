## Calcular el area de un triangulo

base = None
altura = None

while True:
    try:
        base = float(input('escriba la base del triangulo: '))
        break
    except:
        print('Debe de escribir un numero.')

while True:
    try:
        altura = float(input('escriba la altura del triangulo: '))
        break
    except:
        print('Debe de escribir un numero.')

area = base * altura / 2

print("el area del triangulo es igual a {}".format(area))


