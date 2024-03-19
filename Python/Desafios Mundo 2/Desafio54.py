'''Crie um programa que leia o ano de nascimento de sete
pessoas. No final. mostre quantas pessoas ainda não atingiream 
a maioridade e quantas já são maiores'''
s=0

from datetime import date
for c in range(1,8):
  ano = int(input('Em que a {}° pessoa nasceu? ' .format(c)))
  idade = date.today().year - ano
  if idade >= 21:
    s = s + 1
a = 7-s
print('No total, {} pessoas de maior e {} são de menor' .format(s,a))
