from random import choice

n1 = str(input('Digite primeiro nome: '))
n2 = str(input('Digite segundo nome: '))
n3 = str(input('Digite terceiro nome: '))
n4 = str(input('Digite quarto nome: '))

lista = [n1, n2, n3, n4]

escolhido = choice(lista)

print('O nome escolhido foi {}'.format(escolhido)) 
