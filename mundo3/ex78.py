listanum = []
maior = 0
menor = 0 
for c in range(0, 5):
    num = int(input(f"Digite um valor para a posição {c}: "))
    listanum.append(num)
    if c == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f"Você digitou os valores {listanum}")
print(f"O maior valor digitado foi {maior} nas posições ", end="")
for i, v in enumerate(listanum):
    if v == maior:
        print(f"{i}...", end="")
print(f"\nO menor valor digitado foi {menor} nas posições ", end="")
for i, v in enumerate(listanum):
    if v == menor:
        print(f"{i}...", end="")
