'''Desenvolva um programa que leia o nome, idade e
sexo de 4 pessoas. No final do porgrama mostre:
A média de idade do grupo
Qual o nome do homem mais velho
Quantas mulheres tem menos de 20 anos'''
s = 0
maioridadehomem = 0
nomevelho = ''
mulheresnovas = 0
for p in range(1, 5):
    print('{:=^20}' .format(' {}° Pessoa ' .format(p)))
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = str(input('[M/F]')).strip()
    s += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulheresnovas += 1
mediaidade = s/4
print('A média de idade do grupo é de {} anos' .format(mediaidade))
print('O homem mais velho se chama {} e tem {} anos' .format(nomevelho, maioridadehomem))
print('O total de mulheres com meno de 20 anos é de: {} Mulheres' .format(mulheresnovas))