## ordenar 3 numeros de menor a mayor sin usar condicionales ni ciclos

a = int(input())
b = int(input())
c = int(input())

## opcion 1
x= (a,b,c)
print(sorted(x))

## opcion 2

s = min(a,b,c)
o = max(a,b,c)
t = (a+b+c) - o - s
print(s,t,o)