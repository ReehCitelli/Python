primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for c in range(primeiro, primeiro + (razao * 10), razao):
    print(c, end=' → ')

print('ACABOU')
