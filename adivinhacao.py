print('*' *24)
print('* Jogo da adivinhação *')
print('*' *24)
numero_secreto = 42
chute = int(input('Digite o seu número:	'))
print('Você digitou: ', chute)
if (numero_secreto == chute):
    print('Você acertou!')
else:
    print('Você errou!')
