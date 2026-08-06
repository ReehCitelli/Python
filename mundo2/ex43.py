peso = float(input('Qual seu peso (KG): '))
altura = float(input('Qual sua altura (M): '))

imc = peso / (altura ** 2)

print(f'O IMC dessa pessoa é de {imc:.1f}')

if imc < 18.5:
    print('Você está abaixo do peso normal')
elif imc < 25:
    print('Você está na faixa de peso normal')
elif imc < 30:
    print('Você está com sobrepeso')
elif imc < 40:
    print('Você está com obesidade')
else:
    print('Você está em obesidade mórbida')
