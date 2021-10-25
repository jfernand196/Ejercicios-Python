#Obtener el primer y ultimo elemento de una lista

lista = ['juan', 'mateo', 'yamile', 'vero']
primer_elemento = lista[0]
#OPCION 1
#ultimo_elemento = lista[len(lista) -1]
#OPCION 2 CON SLICE
ultimo_elemento = lista[-1]
print(' primer elemento: {} y ultimo elemento: {}'.format(primer_elemento, ultimo_elemento))