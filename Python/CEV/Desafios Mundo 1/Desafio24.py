'''Crie um programa que leia o nome de uma cidade
e diga se ela comça ou não com o nome Santo'''
cidade = str(input('Qual o nome da cidade?'))
cidade1 = cidade.split()
print('A cidade começa com "Santo"? : {}' .format(cidade1[0].find('Santo')))
