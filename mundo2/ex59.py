import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

n1 = int(input('Digite o primeiro valor: '))  # pede o primeiro número antes do menu abrir
n2 = int(input('Digite o segundo valor: '))  # pede o segundo número antes do menu abrir

op = 0  # começa em 0 para garantir que o menu apareça pelo menos uma vez
amarelo = '\033[33m'
reset = '\033[m'

while op != 5:  # repete enquanto a opção escolhida não for 5 (sair)
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
    ''')
    op = int(input('Escolha uma opção: '))  # lê a opção escolhida pelo usuário

    if op == 1:
        limpar_tela()
        print(f'{amarelo}A soma de {n1} + {n2} é {n1 + n2}{reset}')
    elif op == 2:
        limpar_tela()
        print(f'{amarelo}A multiplicação de {n1} * {n2} é {n1 * n2}{reset}')
    elif op == 3:
        limpar_tela()
        if n1 > n2:
            print(f'{amarelo}O número {n1} é maior que {n2}{reset}')
        elif n2 > n1:
            print(f'{amarelo}O número {n2} é maior que {n1}{reset}')
        else:
            print(f'{amarelo}Os números são iguais{reset}')
    elif op == 4:
        limpar_tela()
        n1 = int(input('Digite o primeiro valor: '))  # permite trocar os números a qualquer momento
        n2 = int(input('Digite o segundo valor: '))
    elif op == 5:
        print('Volte sempre')
    else:
        print('Opção inválida!')

