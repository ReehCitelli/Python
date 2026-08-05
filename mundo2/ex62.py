Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.
#############################################
primeiro = int(input('Primeiro termo: '))  # lê o primeiro termo da PA
razao = int(input('Razão: '))  # lê a razão da PA
termo = primeiro  # variável auxiliar para não alterar "primeiro"
c = 1  # contador de termos já mostrados
total = 0  # total de termos a exibir até agora
mais = 10  # quantos termos mostrar nessa rodada (começa com 10)
while mais != 0:  # continua enquanto o usuário quiser mais termos
    total += mais  # soma a nova quantidade ao total
    while c <= total:  # mostra os termos até bater o novo total
        print(f'{termo} → ', end='')  # mostra o termo atual
        termo += razao  # calcula o próximo termo
        c += 1  # incrementa o contador
    print('Pausa')  # indica o fim da rodada
    mais = int(input('Quantos termos voce quer mostrar a mais?: '))  # pergunta se quer continuar
print(f'Prograssão finalizada com {total} termos!')  # mostra o total final de termos
#############################################
