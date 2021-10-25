# diferencia entre funcion MAP() y FILTER()

print(list(map(lambda var: var%2 == 0,range(0,10))))
#[True, False, True, False, True, False, True, False, True, False] 
print(list(filter(lambda var: var%2 == 0,range(0,10))))
#[0, 2, 4, 6, 8] 