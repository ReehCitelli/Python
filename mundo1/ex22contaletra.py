nome = str(input('Digite seu nome: ')).strip()

print('O nome em maiusculo {}'.format(nome.upper())) 
print('O nome em minusculo {}'.format(nome.lower())) 
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' '))) 
#print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) 
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))
