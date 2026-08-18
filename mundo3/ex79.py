numeros = list()
while True:
    n = int(input('Digite um número: ')) 
    if n < 0 or n > 100:  # valida o intervalo permitido
        print('Número fora do intervalo permitido! [0-100]')
        continue  # volta pro início sem processar esse número
    if n not in numeros:
        numeros.append(n)
        print('Número adicionado com sucesso...')   
    else:
        print('Número duplicado! Não vou adicionar...')
    r = ' '
    while r not in 'SN':  # valida a resposta S/N
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break   
numeros.sort()
print(f'Você digitou os valores {numeros}')