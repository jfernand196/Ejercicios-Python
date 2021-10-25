# Generar los n primeros numeros pares positivos

"""
x = []
for i in range(20):
    x.append(i*2) 
print(x)
print(len(x))      
"""

n = 50
x = []
contador = 0
numero = 0
while contador < n:
    if numero % 2 == 0:
        x.append(numero)
        contador += 1
    numero += 1

print(x)
print(len(x))






