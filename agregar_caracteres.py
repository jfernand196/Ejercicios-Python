# Rellenar una cadena de caracteres con un caracter especifico

# python => ***python***

lenguaje = 'python'

print(lenguaje.ljust(6 + 3, '*'))
print(lenguaje.rjust(6 + 3, '*'))
print(lenguaje.ljust(6 + 3, '*').rjust(12,'*'))