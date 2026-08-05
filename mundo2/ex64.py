#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai 
#parar quando o usuário digitar o valor 999, que é a condição de parada. No final, 
#mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
####################################################################################

num = cont = soma = 0  # inicializa as três variáveis com 0
num = int(input('Digite um numero: [ 999 para sair ]: '))  # lê o primeiro número
while num != 999:  # repete até o usuário digitar 999
    soma += num  # acumula o valor na soma
    cont += 1  # conta mais um número digitado
    num = int(input('Digite um numero: [ 999 para sair ]: '))  # lê o próximo número
print(f'Voce digitou {cont} numeros e a soma deles foi {soma}')  # mostra o resultado 

####################################################################################
