jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, total):
    partidas.append(int(input(f'Quantos gols na partida {c + 1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(f'o jogador {jogador["nome"]} jogou {total} partidas.')
for i, g in enumerate(jogador['gols']):
    print(f'    => Na partida {i + 1}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
