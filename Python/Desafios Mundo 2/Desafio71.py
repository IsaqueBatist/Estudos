'''Crie um programa que simule o funcionamento de um caixa eletrônico. No
inicio, pergutne ao usuário qual será o valor a ser sacado 
e o programa vai informar quantas cédulas de cada valor seráo entregues
Considere que o caixa possui cédular de 50, 20, 10 e 1'''
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totaced = 0
while True:
    if total >= ced:
        total -= ced
        totaced += 1
    else:
        if totaced > 0:
            print(f'Total de {totaced} cédulas de R${ced}')
        if ced == 50:
                ced = 20
        elif ced == 20:
                ced = 10
        elif ced == 10:
                ced = 1
        totaced = 0
        if total == 0:
                break
