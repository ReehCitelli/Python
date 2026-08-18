num = list()
pares = list()
impares = list()
resp = str(input('Digite um número: [x para parar] '))
while resp != 'x': # enquanto a resposta for diferente de x, faça:
    num.append(int(resp))
    resp = str(input('Digite um número: [x para parar] '))
    
for n in num: # para cada número na lista:
    if n % 2 == 0: # se o número for par, faça:
        pares.append(n)
    else: # se o número for ímpar, faça:
        impares.append(n)

print(f'Lista completa: {num}')
print(f'Números pares: {pares}')
print(f'Números ímpares: {impares}')