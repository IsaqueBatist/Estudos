'''Crie um programa que leia o nome de uma pessoa e 
diga se ela tem silva no nome'''
nome = str(input('Qual o seu nome?'))
print('O seu nome tem "Silva"? : {}' .format(nome.find('Silva')))