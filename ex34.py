salario = float(input("Digite o salário do funcionário: "))
if salario <= 1250: 
    novo = salario + (salario * 0.15)
else:
    novo = salario + (salario * 0.10)
print(f"O novo salário do funcionário é: R${novo:.2f}")
