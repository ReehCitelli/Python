from datetime import date  # importa a função date do módulo datetime, usada para obter a data atual

atual = date.today().year  # guarda o ano atual do sistema
tmaior = 0  # contador de pessoas maiores de idade
tmenor = 0  # contador de pessoas menores de idade

for pessoas in range(1, 8):  # repete 7 vezes, uma para cada pessoa (o range vai de 1 a 7)
    nasc = int(input('Em que ano a pessoa nasceu?: '))  # lê o ano de nascimento da pessoa
    idade = atual - nasc  # calcula a idade subtraindo o ano de nascimento do ano atual

    if idade >= 21:  # verifica se a idade é maior ou igual a 21
        tmaior += 1  # se for, soma 1 no contador de maiores
    else:  # caso contrário
        tmenor += 1  # soma 1 no contador de menores

print(f'Ao total são {tmaior} pessoas maiores e {tmenor} pessoas menores de idade')  # exibe o resultado final
