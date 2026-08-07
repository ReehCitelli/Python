#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
#################################################################################################################

while True: # repete indefinidamente
    n = int(input('Quer ver a tabuada de qual valor?\n[Digite um valor negativo para sair]: ')) # lê o número
    print('-' * 30) # imprime uma linha de separação
    if n < 0: # se o valor for negativo
        break # interrompe o loop
    for c in range(1, 11): # repete de 1 a 10
        print(f'{n} x {c:2} = {n*c:2}')    # imprime a tabuada do valor digitado
    print('-' * 30) # imprime uma linha de separação
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!') # mensagem de encerramento

#################################################################################################################
