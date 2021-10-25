#Obtener la extension de un archivo especificado por el usuario

nombre_archivo = input('Ingrese el nombre del archivo: ')
partes_nombres_archivo = nombre_archivo.split('.')
print(partes_nombres_archivo)
print(partes_nombres_archivo[-1])
#main.py