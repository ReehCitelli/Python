dias =  int(input('Quantos dias alugado?: '))
km =  float(input('Quantos km rodados?: '))

pago = (dias*60)+(km*0.15)
print('Total a pagar é de {:.2f} reais'.format(pago))
