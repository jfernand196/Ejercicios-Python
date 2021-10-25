# Temperaturas

# Escribe una función llamada `temperaturas` que reciba un arreglo (que representan temperaturas) y 
# retorne `true` si todas las temperaturas están en el rango normal (entre 18 y 30 grados) o `false` de 
# lo contrario.


#     temperaturas([30, 19, 21, 18]) -> true
#     temperaturas([28, 45, 17, 21, 17, 70]) -> false

def temperaturas(x):
    r= []
    for i in x:
        o=0
        if i>= 18 and i<=30:
            r.append(i)
    
    
    return r                  
       

print(temperaturas([30, 19, 21, 18])) #-> true
print(temperaturas([28, 45, 17, 21, 17, 70])) #-> false



