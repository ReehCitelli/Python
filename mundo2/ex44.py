print(f'{"Lojas Renata":=^40}')
preco = float(input('Preço das compras: R$ '))

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
    print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} à vista, com 10% de desconto.')
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} à vista no cartão, com 5% de desconto.')
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}.')
    print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final, sem juros.')
elif opcao == 4:
    numero_parcelas = int(input('Quantas parcelas? '))
    total = preco + (preco * 20 / 100)
    parcela = total / numero_parcelas
    print(f'Sua compra será parcelada em {numero_parcelas}x de R${parcela:.2f}.')
    print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final, com 20% de juros.')
else:
    print('Opção inválida!')
