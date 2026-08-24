from random import randint
from time import sleep
from operator import itemgetter # permite ordenar um dicionário por valor

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:') 
for k, v in jogo.items(): # iterando sobre o dicionário
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # ordenando o dicionário pelo valor, do maior para o menor
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking): # iterando sobre a lista de tuplas
    print(f'   {i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
