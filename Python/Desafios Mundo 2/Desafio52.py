'''Faça um programa que leia um número inteiro diga se lee
é ou não um número primo'''
'''num = int(input('Digite um número'))
if num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
  t = 'É Primo'
else:
  t = 'Não é Primo'
if num == 2 or num ==3 or num ==5:
  t = 'É Primo'
print('O número escohido: {}' .format(t))'''
num = int(input('Digite um número'))
tot = 0
for c in range(1,num+1):
  if num % c ==0:
    print('\033[33m', end=' ')
    tot += 1
  else:
    print('\033[31m', end=' ')
  print(c, end = ' ')
print('\n\033[mO número {} foi divisível {} vezes' .format(num, tot))
if tot == 2:
  print('E por isso ele é PRIMO')
else:
  print('E por isso ele não é primo')