print('*' *23)
print('*\033[35m Jogo da adivinhação\033[m *')
print('*' *23)
numero_secreto = 42
total_de_tentativas	= 3
rodada = 1
while (rodada <= total_de_tentativas):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))

    chute = int(input('Digite o seu número: '))
    print('Você digitou: ', chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print('*' * 16)
        print('* \033[32mVocê acertou\033[m *')

        break
    elif(maior):
        print('*' * 26)
        print('* \033[31mVocê errou! chute alto\033[m *')
        print('*' * 26)
    elif(menor):
        print('*' * 27)
        print('* \033[31mVocê errou! chute baixo\033[m *')
        print('*' * 27)

    rodada = rodada + 1

print('*' *16)
print ('*\033[37m Fim do jogo  \033[m*')
print('*' *16)