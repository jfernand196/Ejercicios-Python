
## formas de usar el print()

degree = 25
newtext = 'los grados son {} celsius'
print(newtext.format(degree))

## agregar decimales

newtext2 = 'los grados son {:.2f} celsius'
print(newtext2.format(degree)) ## 25.00


## multiples valores del metodo .format
quantity = 5
item_number = 150
price = 70
neworder = 'we want {} pieces of item number {} and for {:.2f} dollars'
print()
print(neworder.format(quantity,item_number,price))

# adicionando el mismo valor mas de una ves

edad = 36
nombre = 'juan'
texto = 'hablaremos de {1}. {1} tiene {0} años'
print()
print(texto.format(edad, nombre))

# adicionar valores dentro de .format

texto2 = 'el modelo {model}, del carro {carro}'
print(texto2.format(model = 2005, carro= 'BMW'))
