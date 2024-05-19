'''Faça um programa que leia o nome comppleto de uma 
pessoa, mostrando em seguida o primeiro e o último 
nome separadamente 
ex: ana maria de souza
primeiro = ana
último = souza'''
nome = str(input('Digite seu nome completo: ')).strip()
nomel = nome.split()
print('Primeiro = {}' .format(nomel[0]))
print('Último = {}' .format(nomel[len(nomel)-1]))
