'''Crie um programa que vai gerar cinco números aleatórios e colocar
em uma tupla
Depois disso, mostre a listagem de números gerados também indique o menor
e o maior valor que estão na tupla'''
# Minha resolução
'''from random import randint
contagem = 0
maior = 0
menor = 0
a = ''
while contagem < 5:
    num = str(randint(0, 10))
    a += num + ' '
    b = int(num)
    if contagem == 1:
        maior = b
        menor = b
    elif b > maior:
        maior = b
    elif b < menor:
        menor = b
    contagem += 1
print(f'Os valores sorteados foram {a} sendo {maior} o maior e {menor} o menor')'''
# Resolução Guanabara
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(
    1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {
      max(numeros)}.\nO menor valor sorteado foi {min(numeros)}.')
