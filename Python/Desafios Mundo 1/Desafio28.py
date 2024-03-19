'''Escreva um programa que faça o cmputador 'pensar' em 
um número inteiro entre 0 e 5 e peça para usuário tentar 
descobrir o número escolhido pelo computador. O computador
devera escrever na tela se o usuario venceu ou perdeu'''
from random import randint
from time import sleep
print('-=-' *20)
print('Pensei em um número inteiro de 0 a 6, tente adivinhar')
print('-=-' *20)
numero = randint(0 , 6)
jg = int(input('Qual número você acha que é? '))
print('Prcessando...')
sleep(3)
if numero == jg:
  print('Voce acertou')
else:
  print('Você errou, o número era: ', numero)