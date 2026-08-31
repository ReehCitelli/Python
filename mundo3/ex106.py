c = (
    '\033[m',              # 0 - sem cor (reset)
    '\033[0;30;41m',       # 1 - fundo vermelho
    '\033[1;37;42m',       # 2 - fundo verde (texto branco bright)
    '\033[1;30;43m',       # 3 - fundo amarelo (texto preto bright)
    '\033[1;37;44m',       # 4 - fundo azul (texto branco bright)
    '\033[1;37;45m',       # 5 - fundo roxo (texto branco bright)
    '\033[1;30;47m',       # 6 - fundo branco (texto preto bright)
    '\033[1;37;46m',       # 7 - fundo ciano (texto branco bright)
)

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP  ' , 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Ate logo', 1)