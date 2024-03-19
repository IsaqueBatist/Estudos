'''Faça um progama que ajude um jogador da mega sena a criar palpites
o progrma vai perguntar quantos jogos seram gerados e vai sortear 6 números 
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta'''
from random import randint
lista = []
jogos = list()
quant = int(input('Quantos jogos voce quer que eu sorte'))
total = 1
while total <= quant:
        cont = 0
        while True:
          num = randint(1, 60)
          if num not in lista:
              lista.append(num)
              cont += 1
          if cont >= 6:
              break
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        total+=1
for i,l in enumerate(jogos):
     print(f'Jogo {i+1}: {l}')
