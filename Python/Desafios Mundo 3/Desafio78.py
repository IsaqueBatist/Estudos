'''Faça um programa que liea 5 valores númericos e guarde-os
em uma lista
No final, mostre qual foi o maior e o menor valor digitado
e as suas respectivas posições na lista'''
numeros = []
for cont in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a posição {cont}: ')))
print('=-'*20)
print(f'Os valores digitados foram {numeros}')
print(f'O maior valor digitado foi {max(numeros)}, que se encontra nas posições: ', end ='')
for c,q in enumerate(numeros):
    if q == max(numeros):
        print(c, end=', ')
print(f'\nO menor valor foi {min(numeros)}, que se encontra na posições: ', end='')
for b, r in enumerate(numeros):
    if r == min(numeros):
        print(b, end=' ')

