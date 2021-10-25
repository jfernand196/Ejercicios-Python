#Crear variables a partir de los valores de una lista

numeros = [2, 3, 5, 7]

dos, tres = numeros[:2]
print(dos, tres)

tres, siete = numeros[1], numeros[-1]
print(tres, siete)

tres, _ , siete = numeros[1:]
print(tres, siete)
