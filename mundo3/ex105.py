def notas(*n, sit=False):
    """
    -> Funcao para analizar nota e situações de varios alunos 
    : param n: uma ou mais notas de alunos
    : param sit: valor opcional, indica se deve ou nao adicionar uma situação 
    : return: dicionario com varias informações sobre a situação do aluno
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'Boa'
        elif r['media'] >= 5:
            r['situacao'] = 'Rasoavel'
        else:
            r['situacao'] = 'Ruim'
    return r


resp = notas(5.5, 2.5, 10, sit=True)
print(resp)
help(notas)