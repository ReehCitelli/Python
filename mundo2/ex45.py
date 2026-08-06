from random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura')
pc = randint(0, 2)

# Códigos de cor ANSI
verde = '\033[32m'
vermelho = '\033[31m'
amarelo = '\033[33m'
reset = '\033[m'

print('''Jokenpô:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

voce = int(input('QUAL SUA JOGADA? '))

if voce not in (0, 1, 2):
    print(f'{vermelho}JOGADA INVÁLIDA{reset}')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)

    print('*-' * 12)
    print(f'O computador jogou {itens[pc]}')
    print(f'Você jogou {itens[voce]}')
    print('*-' * 12)

    if pc == voce:
        print(f'{amarelo}Deu empate{reset}')
    elif (pc == 0 and voce == 1) or (pc == 1 and voce == 2) or (pc == 2 and voce == 0):
        print(f'{verde}Você ganhou{reset}')
    else:
        print(f'{vermelho}Você perdeu{reset}')

    print('*-' * 12)
