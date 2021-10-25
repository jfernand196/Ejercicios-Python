from collections import defaultdict

## clase defaultdict o diccionrio por defecto nos sirve para establecer un valor predeterminado a los 
## elementos que van a pertenecer a una collecion o diccionario.

versiones_lenguajes = defaultdict(lambda: '1.0.0') ## valor string, no es numerico
versiones_lenguajes["java"] = "12.0.0"
versiones_lenguajes["php"] = '3.0.2'
versiones_lenguajes['c#']= '4.5.6'

print(len(versiones_lenguajes))
print(versiones_lenguajes)
print(versiones_lenguajes['java'])
print(versiones_lenguajes['php'])
print(versiones_lenguajes['c#'])
print(versiones_lenguajes['python'])## como no aparece en el listado, por defecto se toma '1.0.0'

print()

lenguajes = 'python javascript php c# java c++ c php python python javascript'
lenguajes_separados = lenguajes.split() ## split indica particionamiento sobre el caracter spacio, toma como
##delimitador el caracter spacio
print(lenguajes)
print(lenguajes_separados)

conteo_lenguajes = defaultdict(int) ## con int nos hace conteo con valor numerico 0
for l in lenguajes_separados:
    conteo_lenguajes[l] += 1
print()
print(conteo_lenguajes)
print(conteo_lenguajes['python'])
print(conteo_lenguajes['javascript'])
print(conteo_lenguajes['kotlin']) ## como no aparece en el listado, por defecto se toma cero

## Crear un diccionario predeterminado con valores

puntajes = defaultdict(int, Edward= 80, Daniela= 85, Oliva= 90)

print('Ejemplo creando diccionario con defaultdict')
print(len(puntajes))
print(puntajes['Edward'])
print(puntajes['Daniela'])
print(puntajes['Oliva'])
print(puntajes['German']) # no existe en el diccionario, queda con 0 por inicializar con INT
puntajes['German'] = 75
print(puntajes['German']) # otra forma de agregar un dato a un diccionario

## Iterar sobre un diccionario defaultdict

print('Iterar objetos de un diccionario')

for k, v in conteo_lenguajes.items():
    print('llave: {},- valor: {}'.format(k,v))