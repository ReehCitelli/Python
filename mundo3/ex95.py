time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()  # limpa os dados do jogador anterior
    jogador['nome'] = str(input('Nome do jogador: '))  # lê o nome
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))  # lê o total de partidas
    partidas.clear()  # limpa os gols do jogador anterior
    for c in range(0, total):  # repete para cada partida jogada
        partidas.append(int(input(f'Quantos gols na partida {c + 1}? ')))  # lê e guarda os gols da partida
    jogador['gols'] = partidas[:]  # copia a lista de gols para o dicionário
    jogador['total'] = sum(partidas)  # soma o total de gols do jogador
    time.append(jogador.copy())  # adiciona uma cópia do jogador ao time
    while True:
        resp = str(input('Quer continuar cadastrando jogadores? [S/N] ')).strip().upper()[0]  # lê e valida a resposta
        if resp in 'SN':
            break  # sai do loop de validação quando a resposta for válida
        else:
            print('ERRO! Responda apenas S ou N.')  # avisa se a resposta for inválida
    if resp == 'N':  # verifica a resposta fora do loop de validação
        break  # encerra o cadastro

print('=-' * 30)
print('cod  nome           gols                     total')
print('-' * 60)
for k, v in enumerate(time):  # mostra a lista resumida de todos os jogadores
    print(f'{k:<4} {v["nome"]:<14} {str(v["gols"]):<24} {v["total"]}')
print('=-' * 30)

while True:  # menu para ver detalhes de um jogador específico
    cod = int(input('Mostrar dados de qual jogador? [999 para parar] '))  # lê o código do jogador
    if cod == 999:
        break  # sai do menu de detalhes
    if cod < 0 or cod >= len(time):  # valida se o código existe na lista
        print('ERRO! Código inválido.')
        continue  # volta pro início do menu sem mostrar nada
    print(f' -- LEVANTAMENTO DO JOGADOR {time[cod]["nome"]}')
    for i, g in enumerate(time[cod]['gols']):  # mostra os gols de cada partida do jogador escolhido
        print(f'    Na partida {i + 1}, fez {g} gols.')
    print(f'    Foi um total de {time[cod]["total"]} gols.')

print('=-' * 30)
print('VOLTE SEMPRE!')