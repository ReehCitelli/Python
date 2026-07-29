num = int(input('Digite um número: '))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[33m{c}\033[m', end=' ')
        tot += 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')

print(f'\nO número {num} foi divisível {tot} vezes')

if tot == 2:
    print('Ele é primo')
else:
    print('Ele não é primo')
