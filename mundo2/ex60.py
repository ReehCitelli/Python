#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
############################################################################################################

n = int(input('Digite um número para calcular seu fatorial: '))
c = n  # variável auxiliar para controlar a contagem regressiva sem alterar n
f = 1  # acumulador do resultado do fatorial, começa em 1 (neutro da multiplicação)

print(f'Calculando {n}! = ', end=' ')

while c > 0:  # repete até chegar em 0
    print(f'{c}', end=' ')  # mostra o número atual da contagem
    print(' x ' if c > 1 else ' = ', end=' ')  # mostra "x" entre os números, ou "=" antes do resultado
    f *= c  # multiplica o acumulador pelo número atual
    c -= 1  # decrementa a contagem para o próximo número

print(f'{f}')  # mostra o resultado final do fatorial

############################################################################################################
