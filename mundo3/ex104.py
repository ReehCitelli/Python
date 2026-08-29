def errov(inf): 
    """
    -> Informa o texto passo na variavel -> inf <- na cor vermelha
    """
    print(f'\033[0;31m{inf}\033[m')

def leiaint(msg):
    """
    -> Valida se o valor informado na variavel é to tipo numerico 
    """
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            errov('Erro! Digite um numero valido.')
        if ok:
            break
    return valor


n = leiaint("Digite um numero positivo: ")
print(f'voce acabou de digitar o numero {n}')
