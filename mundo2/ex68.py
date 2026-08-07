# Programa que simula o jogo de Par ou Ímpar entre o jogador e o computador
###########################################################################################

from random import randint
vitórias = 0  # contador de vitórias do jogador
while True:  # repete indefinidamente
    jogador = int(input('Digite um valor: '))  # lê o palpite numérico do jogador
    computador = randint(0, 10)  # sorteia o número do computador
    total = jogador + computador  # soma os dois valores
    tipo = ' '  # variável de controle pra validar a entrada P/I
    while tipo not in 'PI':  # repete até o usuário digitar P ou I
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]  # lê e valida a escolha
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')  # mostra os valores
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')  # mostra se o total deu par ou ímpar
    if tipo == 'P':  # se o jogador escolheu Par
        if total % 2 == 0:  # e o total realmente deu par
            print('Você VENCEU!')
            vitórias += 1  # soma uma vitória
        else:
            print('Você PERDEU!')
            break  # encerra o jogo
    else:  # se o jogador escolheu Ímpar
        if total % 2 != 0:  # e o total realmente deu ímpar
            print('Você VENCEU!')
            vitórias += 1  # soma uma vitória
        else:
            print('Você PERDEU!')
            break  # encerra o jogo
print(f'Game Over! Você venceu {vitórias} vezes.')  # mostra o total de vitórias ao final

###########################################################################################
