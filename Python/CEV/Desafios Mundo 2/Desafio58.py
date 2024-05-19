'''Melhoro o jogo do desafio 28 onde o caomputador vai
pensar em um número entre 0 e 10. Só que a gora o 
jogador vai tentar adivinhar até acertar, mostrando
no final quantos palpites foram necessários para vencer'''
'''from random import randint
from time import sleep
print('{:-^10}' .format('Jogo da adivinhação'))
numc = randint(0,10)
print('Vou pensar em um número e você tem que tentar acertar, Boa Sorte!!!')
print('Pensando...')
sleep(3)
numj = int(input('Qual valor você acha que eu pensei?: '))
tentativas = 1
while numj != numc:
  numj = int(input(('Você errou, tente novamente: ')))
  tentativas += 1
print('Você acertou, o número de tentativas foi de {} vezes' .format(tentativas))'''
from random import randint
palpites = 0
computador = randint(0, 10)
print('Sou seu computador... acabei de pensar em um número entre 0 e 10')
print('Será que voce consegue adivinhar qual foi?')
acertou = False
while not acertou:
    jogador = int(input('Qual é o seu palpite?'))
    palpites += 1
    if jogador == computador:
        acertou = True
    elif jogador < computador:
        print('Mais.. Tente mais uma vez: ')
    elif jogador > computador:
        print('Menos... Tente mai suma vez: ')
print('Acertou!! Com {} tentativas' .format(palpites))
