def fatorial(n, show=False):
    """
    --> Calcula o fatorial de um numero .
    : para n: o numero a ser calculado
    : para show: (opcional) mostra ou nao a conta
    : para return: retorna o valor do fatorial do n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


help(fatorial)
print(fatorial(5,True))
