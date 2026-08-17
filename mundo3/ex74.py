from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)) # numeros aleatórios entre 1 e 10
print(f'Os números sorteados foram: {numeros}') # numeros sorteados
print(f'O maior número sorteado foi: {max(numeros)}')  # maior número
print(f'O menor número sorteado foi: {min(numeros)}')
