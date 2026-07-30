sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]  # lê o sexo, remove espaços, deixa maiúsculo e pega só o 1º caractere

while sexo not in 'FM':  # repete enquanto o valor digitado não for 'F' nem 'M'
    sexo = str(input('Dados incorretos. Digite seu sexo [M/F]: ')).strip().upper()[0]  # pede novamente até vir um valor válido

print(f'Sexo {sexo} registrado com sucesso.')  # exibe a confirmação do sexo registrado
