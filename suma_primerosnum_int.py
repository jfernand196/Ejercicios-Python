# Calcular la suma de los primeros numeros enteros

# Usando la formula de Gauss: n*(n+1)/2

n = 10
suma = n*(n+1)/2
print(suma)

## usar la funcion sum

suma = sum(range(1, n+1))

#
x = int(input('ingresar un numero: '))
y = [i for i in range(1, x+1)]
cont = 0
for _ in y:
    cont += _
print(y)
print('la suma de los {} primeros numeros enteros es: {}'.format(x,cont))
print(__file__)




