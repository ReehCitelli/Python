#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
##################################################################################

n = int(input('Quantos termos voce quer mostrar?: '))  # lê quantos termos mostrar
t1 = 0  # primeiro termo da sequência
t2 = 1  # segundo termo da sequência
print(f'{t1} -> {t2}', end='')  # mostra os dois primeiros termos
c = 3  # contador, começa em 3 pois os 2 primeiros já foram exibidos
while c <= n:  # repete até completar os n termos
    t3 = t1 + t2  # calcula o novo termo somando os dois anteriores
    print(f' -> {t3}', end='')  # mostra o novo termo
    t1 = t2  # avança t1 para o valor de t2
    t2 = t3  # avança t2 para o novo termo calculado
    c += 1  # incrementa o contador 
print('Fim')  # indica o fim da sequência

##################################################################################
