from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print(f'Ainda faltam {saldo} anos para o alistamento.')
    print(f'Seu alistamento será em {ano}.')
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    print(f'Seu alistamento foi em {ano}.')
