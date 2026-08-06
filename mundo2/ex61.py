Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 
primeiros termos da progressão usando a estrutura while.
#################################################################################
primeiro = int(input('Primeiro termo: '))  # lê o primeiro termo da PA
razao = int(input('Razão: '))  # lê a razão da PA
termo = primeiro  # variável auxiliar para não alterar "primeiro"
c = 1  # contador de termos já mostrados
while c <= 10:  # repete 10 vezes
    print(f'{termo} → ', end='')  # mostra o termo atual
    termo += razao  # calcula o próximo termo
    c += 1  # incrementa o contador
print('fim')  # mostra que a sequência acabou
#################################################################################
