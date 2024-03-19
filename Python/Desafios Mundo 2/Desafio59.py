'''Crie um programa que leia dois valores e mostre um menu
na tela:
1 somar
2 multiplicar
3 maior
4 novos números
5 sair do programa
 Seu programa deverá realizar a operação solicitada em cada caso'''
from time import sleep
escolha = 0
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
while escolha != 5:
    maior = n1
    if n1 < n2:
        maior = n2
        print('-=--' *10)
    print('''O que deseja fazer?)
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair do programa''')
    escolha = int(input('>>>>>Sua opção: '))
    if escolha == 1:
        print('A soma entre {} e {} é: {}' .format(n1, n2, n1+n2))
    elif escolha == 2:
        print('A multiplicação entre {} e {} é: {}'.format(n1, n2, n1*n2))
    elif escolha == 3:
        print('O maior número entre {} e {} é: {}' .format(n1, n2, maior))
    elif escolha == 4:
        print('Ok, Digite mais dois números: ')
        n1 = float(input('Primeiro número: '))
        n2 = float(input('Segundo número: '))
    elif escolha == 5:
        print('Saindo do Programa....')
        sleep(2)
        print('FIM')
    else:
        print('Opção Inválida')
