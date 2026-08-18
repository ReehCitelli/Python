valores = [] # Lista para armazenar os valores digitados
while True:
    valores.append(int(input('Digite um valor: '))) # Adiciona o valor digitado à lista
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0] # Pega a primeira letra da resposta e converte para maiúscula
    if resp in 'N':
        break
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True) # Ordena a lista em ordem decrescente
print(f'Os valores em ordem decrescente são {valores}.')
if 5 in valores: # Verifica se o valor 5 está na lista
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista.')
