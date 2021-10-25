# simular la funcion join

numeros = [2,4,5,77]

#opcion 1
#print('juan'.join([str(n) for n in numeros]))
#print('juan'.join(numeros))

#opcion 2

def concatenar_listas(lista):
    resultado= ''
    for i in lista:
        resultado +=str(i)
    return resultado

numeros = [2,4,5,77]
print(concatenar_listas(numeros))
