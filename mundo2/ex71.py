valor = int(input("Digite um valor: "))
total = valor
cedulas = 50
cont = 0
while True:
    if total >= cedulas:
        total -= cedulas
        cont += 1
    else:
        if cont > 0:
            print(f'Total de {cont} cédulas de R${cedulas}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        cont = 0
        if total == 0:
            break
