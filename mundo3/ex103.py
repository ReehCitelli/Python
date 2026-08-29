def ficha(j='<null>', gol = 0):
    print(f'O jogador {j} fez {gol} gols')


nome = str(input("Nome do jogador: "))
g = str(input("Quantos gols ele marcou: "))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if nome.strip() == '':
    ficha(gol=g)
else:
    ficha(nome,g)
    