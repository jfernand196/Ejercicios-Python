# 1. Calcula los impuestos
# Escribe una función llamada calcular_impuestos que reciba dos argumentos numéricos: edad e ingresos. 
# Si edad es igual o mayor a 18 y los ingresos son iguales o mayores a 1000 debe retornar ingresos * 40%. 
# De lo contrario retorna 0.
# calcular_impuestos(18, 1000) # retorna 400
# calcular_impuestos(40, 10000) # retorna 4000
# calcular_impuestos(17, 5000) # retorna 0

def calcular_impuestos(edad, ingresos):
        if edad >= 18 and ingresos >= 1000: return int(ingresos * 0.40)
        else: return 0

print(calcular_impuestos(18, 1000))
print(calcular_impuestos(40, 10000))
print(calcular_impuestos(17, 5000))
