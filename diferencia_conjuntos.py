# Calcular la diferencia de conjunto de colores

color1 = ["negro","blanco","verde","azul"]
color2 = ["rojo","cafe","verde","azul","naranja","rosa"]

conjunto_color1 = set(color1)
conjunto_color2 = set(color2)

resultado = conjunto_color1.difference(conjunto_color2)
resultado2= conjunto_color1 - conjunto_color2

print(resultado)
print(resultado2)
