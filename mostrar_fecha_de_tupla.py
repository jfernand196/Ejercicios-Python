#Mostrar la fecha de un evento almacenado en una tupla

fecha_evento = (2013, 9, 10)
print(type(fecha_evento))
print(fecha_evento)
print('el evento sera en la fecha: ',fecha_evento)
print('el evento sera en la fecha: %i/%i/%i' % fecha_evento)

#OPCION 2
año, mes, dia = fecha_evento
print('el evento sera en la fecha: {}/{}/{}'.format(año,mes,dia))
