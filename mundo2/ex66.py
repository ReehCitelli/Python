#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
#####################################################################################

cont = soma =0  # inicializa as duas variáveis com 0
while True: # repete indefinidamente
    num = int(input('Digite um numero: [ 999 para sair ]: ')) # lê o número
    if num == 999: # se o número for 999
        break # interrompe o loop
    cont += 1 # conta mais um número digitado
    soma += num # acumula o valor na soma
print(f'Voce digitou {cont} numeros e a soma deles foi {soma}')  # mostra o resultado

#####################################################################################
