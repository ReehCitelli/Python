n = int(input('Digite um número de 1 a 9: '))
print('-' * 11)
for c in range(1, 11):
    print(f'{n} x {c:2} = {n*c:2}')
