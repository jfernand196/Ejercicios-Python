# Crear una funcion para sumer unicamente numeros enteros

def sumar(x, y):

    if isinstance(x, int) and isinstance(y, int):
        return x + y
    else:
        raise TypeError('Los valores deben ser enteros')

try:
    print(sumar(5,4))
    print(sumar(5, '4'))
except TypeError as e:
    print(e)