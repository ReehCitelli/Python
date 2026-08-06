from random import randint

acertou = False  # controla se o jogador já acertou o número
palpite = 0  # conta quantas tentativas o jogador fez

computador = randint(0, 10)  # o computador "pensa" em um número aleatório entre 0 e 10

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)

while not acertou:  # repete enquanto o jogador ainda não tiver acertado
    jogador = int(input('Em que número eu pensei? '))  # lê o palpite do jogador
    palpite += 1  # soma 1 na contagem de tentativas

    if jogador == computador:  # se o palpite for igual ao número pensado
        acertou = True  # marca que o jogador acertou, encerrando o loop
    else:
        if jogador < computador:  # se o palpite foi menor que o número pensado
            print('Maaaaiisss....')  # pede para o jogador tentar um número maior
        else:  # se o palpite foi maior que o número pensado
            print('Meennooossss...')  # pede para o jogador tentar um número menor

print(f'Acertou com {palpite} tentativas, parabéns!')  # exibe quantas tentativas foram necessárias
