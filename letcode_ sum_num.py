

lista = [3,2,3]
sum = 6
resul = []

for i in lista:
    for e in range(len(lista)):
        resultado = i + lista[e]
        if resultado == sum:
            resul = [e, lista.index(i)]
print(resul)
           
        