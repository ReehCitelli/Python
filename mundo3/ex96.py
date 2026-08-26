def area(larg, comp): # parametro passado por l e c
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')
#sempre dar 2 linhas de espaço entre funções

l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c) 


