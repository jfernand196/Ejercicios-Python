# Programa que le pide al usuario la edad (edad entero) y comprueba
#si ese usuario es mayor de edad (18 años)



try:
    numero = int(input('introduce tu edad: ')) 
    
except ValueError:
    print('no has introduciod un nuemero entero')

else:
    if numero >= 18:
        print('eres mayo de edad')
    else:
        print('no eres mayor de edad') 
    
finally:
    print('el codigo ha terminado') ## finally se ejecuta siempre
