lista = []
for c in range(0, 5): # Loop para ler 5 valores
    N = int(input('Digite um valor: '))
    if c == 0 or N > lista[-1]: # Se for o primeiro valor ou se for maior que o último da lista
        lista.append(N)
        print('Adicionado ao final da lista...')   
    else: # Se não for o primeiro valor e for menor ou igual ao último da lista
        pos = 0
        while pos < len(lista): # Loop para encontrar a posição correta para inserir o valor
            if N <= lista[pos]: # Se o valor for menor ou igual ao valor na posição atual da lista
                lista.insert(pos, N) # Insere o valor na posição correta da lista
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}') # Exibe a lista ordenada