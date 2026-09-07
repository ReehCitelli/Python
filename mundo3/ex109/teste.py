from ex109 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é R${moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é R${moeda.dobro(p, True)}')
print(f'Almentando 10%,temos {moeda.aumentar(p, 10, True)}')