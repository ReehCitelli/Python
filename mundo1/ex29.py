velocidade = float(input("Digite a velocidade do carro em km/h: "))
if velocidade > 80:
    print("Multa de R$ 7,00 por cada km acima do limite.")
    multa = (velocidade - 80) * 7
    print(f"Valor da multa: R$ {multa:.2f}")    
else:    
    print("Velocidade dentro do limite permitido. Sem multa.")         
