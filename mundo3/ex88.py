from random import randint
lista = list()
jogos = list()
qtde = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1
while total <= qtde:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print(f'Os jogos sorteados foram: ')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
