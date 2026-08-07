total = cont = totmil = menor = 0
produto = ''

while True:
    produto = input("Digite o nome do produto : ")
    preco = float(input("Digite o preço do produto : "))
    cont += 1 # Contador de produtos
    total += preco # Total gasto na compra
    if preco > 1000: # Se o preço for maior que 1000
        totmil += 1 # Contador de produtos acima de 1000
    if cont == 1 or preco < menor: # Se for o primeiro produto ou se o preço for menor que o menor preço registrado
        menor = preco # Atualiza o menor preço
        barato = produto # Atualiza o nome do produto mais barato   
    resp = ' '
    while resp not in 'SN': # Enquanto a resposta não for S ou N
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break # Sai do loop se a resposta for N

print('-' * 30)
print(f'O total gasto na compra foi de R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')

