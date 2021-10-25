import datetime

#FECHA ACTUAL CON HORA
ahora = datetime.datetime.now()
print(ahora)
#OUPUT 2021-08-13 15:27:10.601234

print(type(ahora))

#Formatear fecha
print(ahora.strftime('%d/%m/%Y %H:%M:%S'))