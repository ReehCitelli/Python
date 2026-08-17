#lista de 20 times do campeonato brasileiro de futebol
times = ('Palmeiras', 'Corinthians', 'Flamengo', 'Fluminense', 'Atlético-MG',
         'Athletico-PR', 'Fortaleza', 'Santos', 'São Paulo', 'Internacional', 'Grêmio', 'Cruzeiro', 'Vasco da Gama',
         'Botafogo', 'Bahia', 'Ceará', 'Atlético-GO', 'Coritiba', 'Sport', 'América-MG')
print('Lista de times do Campeonato Brasileiro:')       
print(times) # imprime a lista de times

print('=' * 30) # imprime uma linha de separação 
print('os 5 primeiros colocados são:')
print('=' * 30) # imprime uma linha de separação 
   
for pos, time in enumerate(times[:5]): # percorre os 5 primeiros times
    print(f'{pos + 1}º - {time}') # exibe a posição e o nome do time

print('=' * 30) # imprime uma linha de separação 
print('os 4 últimos colocados são:')
print('=' * 30) # imprime uma linha de separação 

for pos, time in enumerate(times[-4:]): # percorre os 4 últimos times
    print(f'{pos + 17}º - {time}') # exibe a posição e o nome do time

print('=' * 30) # imprime uma linha de separação 
print('os times em ordem alfabética são:')
print('=' * 30) # imprime uma linha de separação 

for pos, time in enumerate(sorted(times)): # percorre os times em ordem alfabética
    print(f'{pos + 1}º - {time}') # exibe a posição e o nome do time

print('=' * 30) # imprime uma linha de separação 
print(f'o time do {times[9]} está na {times.index(times[9]) + 1}ª posição') # exibe a posição do time solicitado
print('=' * 30) # imprime uma linha de separação 