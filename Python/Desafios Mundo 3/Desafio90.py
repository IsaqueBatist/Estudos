'''Faça um programa que leia nome e média de um aluno,
guardando também a stiruação em um dicionário. No final, 
mostre o conteudo da estrutura na tela'''
# Minha resolução
'''aluno = []
temp = {}
temp['Nome'] = str(input('Nome: '))
temp['Média'] = float(input('Média: '))
if temp['Média'] >= 7:
    situacao = 'APROVADO'
else:
    situacao = 'REPROVADO'
    temp['Situação'] = situacao
    aluno.append(temp.copy())
for e in aluno:
  for k,v in e.items():
    print(f'{k} é igual a {v}')'''
# Resolução Guanabara
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
if aluno['media'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
for k,v in aluno.items():
    print(f'{k} [e igual a {v}]')
