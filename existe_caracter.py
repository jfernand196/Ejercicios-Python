#Comprobar si un caracter dado existe en una cadena de caracteres

lenguaje = 'esTudiando pyhon'

print(lenguaje.count('t'))
print(lenguaje.count('T'))
print(lenguaje.count('t') > 0)
print(lenguaje.count('T') > 0)
print()
print(any(c == 't' for c in lenguaje))
print(any(c.lower() == 't' for c in lenguaje))


