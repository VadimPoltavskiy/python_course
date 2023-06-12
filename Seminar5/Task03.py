def posledov(lenght):
    if lenght == 0:
        return ''
    peremen = input ("Введите чтьо-то: ")
    return posledov(lenght - 1) + peremen + " "

print (posledov(4))