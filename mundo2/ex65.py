# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O 
# programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
####################################################################################

resposta = 'S'  # controla o loop, começa como 's' pra entrar pelo menos uma vez
soma = qtd = media = maior = menor = 0  # inicializa tudo com 0
while resposta in 'Ss':  # repete enquanto o usuário quiser continuar
    num = int(input('Digite um numero: '))  # lê o número
    soma += num  # acumula na soma
    qtd += 1  # conta mais um número
    if qtd == 1:  # no primeiro número, maior e menor começam com ele
        maior = menor = num
    else:
        if num > maior:  # atualiza o maior, se for o caso
            maior = num
        if num < menor:  # atualiza o menor, se for o caso
            menor = num
    resposta = str(input('Quer continuar? [N/S] ')).upper().strip()[0]  # pega só o 1º caractere, maiúsculo e sem espaços
media = soma / qtd  # calcula a média
print(f'Voce digitou {qtd} e a media foi {media:.2f}')  # mostra a quantidade e a média
print(f'O maior valor foi {maior} e o menor foi {menor}')  # mostra o maior e o menor

####################################################################################
