'''Crie um programa que leia nome, sexo e idade de várias pessoas
guardando dados de cada pessoa em um dicionário e todos
os dicionários em uma lista. No final mostre:
Quantas pessoas foram cadastradas
A média de idaade do grupo
Uma lista com toodas as mulheres
Uma lista com todas as pessoas com idade acima da média'''
# Minha resolução
'''Pessoas = dict()
dados = list()
mulheres = list()
contador = idades = 0
while True:
    Pessoas['Nome'] = str(input('Nome: '))
    Pessoas['idade'] = int(input('Idade: '))
    Pessoas['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
    if Pessoas['Sexo'] == 'F':
        mulheres.append(Pessoas['Nome'])
    contador += 1
    idades += Pessoas['idade']
    dados.append(Pessoas.copy())
    opcao = str(input('Quer continuar? [S/N] ')).upper()
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper()
    if opcao == 'N':
        break
media = idades/contador
c = 0
print(f'O grupo tem {contador} pessoas')
print(f'A média de idade é de {media:.2f}')
print(f'As mulheres cadastradas foram: {mulheres}')
print(f'Lista de pessoas que estão acima da média em idade: ')'''
# Resolução guanabara
galera = list()
pessoa = dict()
soma = media = 0
while True:
    #leitura de dados
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    resp = str(input('Deseja continuar? [S/N] ')).upper()[0]
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).upper()[0]
    if resp == 'N':
        break
    #lresultados 
media = soma/len(galera)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
print(f'A média das idades é {media:.2f} anos')
print(f'As mulheres cadastradas foram', end=0)
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["Nome"]}')
print()
print('Listas das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('       ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end=' ')
        print()
