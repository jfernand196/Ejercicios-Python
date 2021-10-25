# Imprimir el calendario con un año y mes en especifico

import calendar

agnio = int(input('escriba el año'))
mes = int(input('escriba el mes'))

print(calendar.month(agnio, mes))