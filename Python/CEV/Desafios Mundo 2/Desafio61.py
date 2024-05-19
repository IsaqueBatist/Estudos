'''Refaça o desafio 51, lendo o primeiro termo
e a razao de uma PA, mostrando os 10 primeiros termos 
da progressão usando a estrutura while'''
print('{}' .format('Gerador de PA'))
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
#decimo = pt + (10-1) * r
contador = 1
while contador <= 10:
    print('{}' .format(pt), end=' -> ')
    pt += r
    contador += 1
print('fim')
