preco =  float(input('Qual o preço do produto? '))
desc = preco -(preco*5/100)
print('Valor: {:.2f} - 5 off total: {:.2f}'.format(preco,desc))
