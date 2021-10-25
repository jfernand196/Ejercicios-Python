def reverse_words_order_and_swap_cases(sentence):
    x = str(sentence)
    minuscula = 'abcdefghijklmnñopqrstwxyz'
    mayuscula = 'ABCDEFGHIJKLMNÑOPQRSTWXYZ'
    y = x.split()
    palabra = ''
    for i in x:
        if i in minuscula:
            palabra += i.upper()
        if i in mayuscula:
            palabra += i.lower()
        if i == ' ':
            palabra += i
    g = palabra.split()
    rev1 = str(reversed(g))
    print(rev1)
    for k in range(len(rev1)):
        return print(rev1[k], end=' ')

reverse_words_order_and_swap_cases('aWESOME is cODING')
