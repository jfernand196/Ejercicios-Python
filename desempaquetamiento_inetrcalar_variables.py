# Desempaquetar una tupla, lista ....
x = [1, 3,'a', True]
print(type(x))

a,b,c,d = x

print(type(a),b,type(c),type(d))

## Intercalar datos

a = 3
b = 2

# se intercambia opcion 1
temp = a
a = b
b = temp

# se intercambia opcion 2
a = 3
b = 2

a , b = b, a


