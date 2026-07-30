for pessoa in range(1, 6):  # repete 5 vezes, uma para cada pessoa
    peso = float(input(f'Digite o peso da {pessoa}ª pessoa: '))  # lê o peso digitado

    if pessoa == 1:  # na primeira pessoa, ainda não temos maior/menor para comparar
        maior = peso  # então o primeiro peso já começa sendo o maior
        menor = peso  # e também o menor
    else:
        if peso > maior:  # se o peso atual for maior que o maior já registrado
            maior = peso  # atualiza o maior
        if peso < menor:  # se o peso atual for menor que o menor já registrado
            menor = peso  # atualiza o menor

print(f'O maior peso lido foi {maior:.1f} kg')  # mostra o maior peso encontrado
print(f'O menor peso lido foi {menor:.1f} kg')  # mostra o menor peso encontrado
