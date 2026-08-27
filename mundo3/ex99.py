from time import sleep
def linha():
    print('*-' * 17)

def maior(* num): 
    cont = maior = 0
    linha()
    print('Analisando valores passados... ')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor 
        else:
            if valor > maior:
                maior = valor 
        cont += 1  
    print()
    linha()
    print(f'foram informados {cont} valores ao todo ')
    print(f'o maior valor informado foi {maior}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(0)
maior()