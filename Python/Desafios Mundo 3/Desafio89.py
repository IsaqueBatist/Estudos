'''Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta. No final, mostre um boletim contendo 
a média de cada um e permita que o usuário possa mostrar as notas de cada
aluno individualmente
'''
dados = []
temp = []
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Nota1: ')))
    temp.append(float(input('Nota2: ')))
    dados.append(temp[:])
    temp.clear()
    opcao = str(input('Quer continuar [S/N]? ').upper())
    while opcao not in 'SN':
        opcao = str(input('Quer continuar [S/N]? ').upper())
    if opcao == 'N':
        break
print('{:<5}{:^20}{:>10}' .format('No.', 'Nome', 'Média'))
print('-'*40)
for n, a in enumerate(dados):
    media = (a[1] + a[2])/2
    print(f'{n:<5} {a[0]:^20} {media:>10}')
print('-'*40)
while True:
    a = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    if a == 999:
        break
    print(f'Notas de {dados[a][0]} são {dados[a][1]}, {dados[a][2]}')
    print('-'*40)
