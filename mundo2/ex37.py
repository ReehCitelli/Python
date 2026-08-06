num = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão
[1] Binário
[2] Octal
[3] Hexadecimal''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{num} convertido para binário: {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para octal: {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para hexadecimal: {hex(num)[2:]}')
else:
    print('Opção inválida')
