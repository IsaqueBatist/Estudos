'''Faça um programa que tenha uma função notas() que pode receber
várias notas de alunos e vai retornar um dicionário com as seguntes informações
Quantidade de notas
A maior nota
A MENOR nota
A média da turma'
A situação (opcional) >7: boa | 
Adicione também as docstrings da funçao'''

def notas(*num, sit=False):
    tudo = {}
    tudo['Total'] = len(num)
    tudo['Maior'] = max(num)
    tudo['Menor'] = min(num)
    tudo['Média'] = sum(num)/len(num)
    if sit == True:
        if tudo['Média'] >= 7:
            si = 'Boa'
        elif 4 < tudo['Média'] >= 5:
            si = 'Razoável'
        elif tudo['Média'] < 5:
            si = 'RUIM'
        tudo['Situação'] = si
    return tudo


rsp = notas(3.5, 2, 6.5, 2, 3, 4, 1, 3, 4, 5, 6)
print(rsp)
