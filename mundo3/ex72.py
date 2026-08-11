extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 
           'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 
           'dezessete', 'dezoito', 'dezenove', 'vinte')
num = 0
while num != 999: # verifica a flag de saída antes de validar o intervalo
    num = int(input('Digite um número entre 0 e 20: [999 para sair] ')) # solicita um número ao usuário
    if num == 999:  # verifica a flag de saída antes de validar o intervalo
        break
    while num < 0 or num > 20: # verifica se o número está fora do intervalo permitido 
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {extenso[num]}')
print('Fim do programa.')