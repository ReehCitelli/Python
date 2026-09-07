def aumentar(preco=0, taxa=0,fmt=False):
    res = preco + (preco * taxa / 100)
    return res if not fmt else moeda(res)

def diminuir(preco=0, taxa=0,fmt=False):
    res = preco - (preco * taxa / 100)
    return res if not fmt else moeda(res)

def dobro(preco=0,fmt=False):
    res = preco * 2
    return res if not fmt else moeda(res)

def metade(preco=0,fmt=False):
    res = preco / 2
    return res if not fmt else moeda(res)

def moeda(preco=0,moeda='R$'):
    return f'R${preco:.2f}'.replace('.', ',')

def resumo(preco=0, taxaa=10, taxar=5):
    print(f'-'*30)
    print('RESUMO DO VALOR'.center(30))
    print(f'-'*30)
    print(f'Preço analizado: \t{moeda(preco)}')
    print(f'O dobro do preço: \t{dobro(preco, True)}')
    print(f'A metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de aumento: \t\t{diminuir(preco, taxar, True)}')
    print(f'-' * 30)