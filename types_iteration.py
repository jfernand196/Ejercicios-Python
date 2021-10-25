# seleccionar numeros pares y multiplicarlos por 3, resultado en otra lista
#Ciclo FOR, append: para agregar datos a una lista


numeros = [8, 2, 7, 20, 4, 2, 9, 21]
print(type(numeros))
print(len(numeros))
print(numeros)

pares_triplicados = []
for n in numeros:
    if n % 2 == 0:
        pares_triplicados.append(n * 3)

print(type(pares_triplicados))
print(len(pares_triplicados))
print(pares_triplicados)

# mismo ejercicio solucionado con listas de compresion (list comprenjention)

pares_triplicados = [n * 3 for n in numeros if n % 2 == 0]
print() # espacio

print(type(pares_triplicados))
print(len(pares_triplicados))
print(pares_triplicados)

# Solucion con ciclos for (iterativa), con 2 listas
#Encontrar los elementos comunes entre las 2 listas

numero_1 = [2, 3, 5, 7, 11]
numero_2 = [2, 7, 13, 19, 23, 3]

interseccion = []

for n1 in numero_1:
    for n2 in numero_2:
        if n1 == n2 and n1 not in interseccion:
            interseccion.append(n1)
print()
print("solucion con ciclo for")
print(len(interseccion))
print(interseccion)


# mismo ejercicio usando listas de comprension (list comprenjention)
#Encontrar los elementos comunes entre las 2 listas
numero_1 = [2, 3, 5, 7, 11]
numero_2 = [2, 7, 13, 19, 23, 3]

interseccion = [n1 for n2 in numero_2 for n1 in numero_1 if n1 == n2]

print()
print("Solucion con listas de compresion")
print(len(interseccion))
print(interseccion)


# mismo ejercicio usando metodo de conjuntos
#Encontrar los elementos comunes entre las 2 listas

numero_1 = [2, 3, 5, 7, 11]
numero_2 = [2, 7, 13, 19, 23, 3]


set(numero_1) # conjunto 1
set(numero_2) # conjunto 2
resultado = set(numero_1) & set(numero_2)
print()
print("Solucion con conjuntos")
print(len(resultado))
print(resultado)

## FIN DE LAS DEMOSTRACIONES CON ITERACION DE LISTAS

fruitstup = ('lemon', 'orange', 'banana')
newit = iter(fruitstup)
print()
print(next(newit))
print(next(newit))
print(next(newit))

frutas = 'frutas' ## Iterar sobre string
iteracion = iter(frutas)
print()
print(next(iteracion))
print(next(iteracion))
print(next(iteracion))