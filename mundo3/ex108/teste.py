import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é R${moeda.metade(p)}')
print(f'O dobro de {moeda.moeda(p)} é R${moeda.dobro(p)}')
print(f'Almentando 10%,temos {moeda.moeda(moeda.aumentar(p, 10))}')