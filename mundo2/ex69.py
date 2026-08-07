tot18 = totH = totM20 = 0 # contador de pessoas com mais de 18 anos, homens cadastrados e mulheres com menos de 20 anos
while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF': # repete até o usuário digitar M ou F
        sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0] 
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' ' # variável de controle pra validar a entrada S/N
    while resp not in 'SN': # repete até o usuário digitar S ou N
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados.')
print(f'E temos {totM20} mulheres com menos de 20 anos.')
