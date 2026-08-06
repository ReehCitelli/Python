maior_idade_homem = 0  # guarda a maior idade encontrada entre os homens
nome_homem_mais_velho = ''  # guarda o nome do homem mais velho até agora
soma_idades = 0  # acumula a soma de todas as idades, para calcular a média depois
mulheres_menores_20 = 0  # contador de mulheres com menos de 20 anos

for pessoa in range(1, 5):  # repete 4 vezes, uma para cada pessoa
    print(f'--- {pessoa}ª pessoa ---')
    nome = str(input('Nome: ')).strip()  # lê o nome e remove espaços extras nas pontas
    idade = int(input('Idade: '))  # lê a idade da pessoa
    sexo = str(input('Sexo [M/F]: ')).strip().upper()  # lê o sexo e padroniza em maiúsculo

    soma_idades += idade  # acumula a idade no total da soma

    if sexo == 'M' and idade > maior_idade_homem:  # se for homem e mais velho que o registrado até agora
        maior_idade_homem = idade  # atualiza a maior idade encontrada
        nome_homem_mais_velho = nome  # guarda o nome dessa pessoa

    if sexo == 'F' and idade < 20:  # se for mulher e tiver menos de 20 anos
        mulheres_menores_20 += 1  # soma 1 no contador

media_idades = soma_idades / 4  # calcula a média dividindo a soma pelo total de pessoas

print(f'A média de idade do grupo é {media_idades:.1f} anos')
print(f'O homem mais velho se chama {nome_homem_mais_velho}, com {maior_idade_homem} anos')
print(f'Ao todo, {mulheres_menores_20} mulher(es) têm menos de 20 anos')
